import streamlit as st
import openai
import requests
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Secure API Keys
openai_api_key = os.getenv("OPENAI_API_KEY")  # Fetch from .env
google_api_key = os.getenv("GOOGLE_API_KEY")  # Fetch from .env

# Ensure API key is set
if not openai_api_key:
    st.error("Missing OpenAI API Key. Check your .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=openai_api_key)

# Function to refine user inputs
def refine_user_inputs(user_input):
    system_prompt = """
    You are an AI travel assistant. Your job is to extract and refine travel details from users.
    Ask clarifying questions if needed and ensure you have:
    - Budget (low, moderate, luxury)
    - Trip duration or travel dates
    - Destination & starting location
    - Purpose (leisure, adventure, honeymoon, business, cultural, etc.)
    - Preferences (food, activities, hidden gems, famous spots, etc.)
    - Dietary preferences or mobility concerns

    Respond in a structured format.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content  # Return structured response


# Function to fetch travel recommendations
def fetch_travel_recommendations(destination, preferences):
    search_query = f"Top attractions and activities in {destination} for {preferences}"
    url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={google_api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch travel recommendations."}


# Function to generate itinerary
def generate_itinerary(user_inputs):
    itinerary_prompt = f"""
    Based on the following user details, generate a structured, day-by-day itinerary:

    {user_inputs}

    Ensure:
    - Logical grouping of activities.
    - Time slots for each activity.
    - Meals & breaks included.
    - Personalization based on user preferences.

    Output in a structured format.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert travel planner."},
            {"role": "user", "content": itinerary_prompt}
        ]
    )

    return response.choices[0].message.content  # Return itinerary


# Streamlit UI
st.title("AI Travel Planner")

user_input = st.text_area("Tell me about your trip details:")

if st.button("Plan My Trip"):
    with st.spinner("Refining your travel details..."):
        refined_inputs = refine_user_inputs(user_input)
        st.write("**Refined Details:**")
        st.write(refined_inputs)

    with st.spinner("Fetching travel recommendations..."):
        # Extract destination and preferences safely
        details = refined_inputs.split("\n")
        destination = details[2] if len(details) > 2 else "Unknown"
        preferences = details[4] if len(details) > 4 else "General"

        recommendations = fetch_travel_recommendations(destination, preferences)
        st.write("**Top Recommendations:**")
        st.json(recommendations)

    with st.spinner("Generating itinerary..."):
        itinerary = generate_itinerary(refined_inputs)
        st.write("**Your Personalized Itinerary:**")
        st.write(itinerary)
