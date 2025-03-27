# AI Travel Planner

## Overview
AI Travel Planner is a **Streamlit** web application that helps users plan their trips by providing **personalized itineraries** based on their preferences. It utilizes **OpenAI's GPT-4** for refining user inputs and generating itineraries, and **Google Search API** for fetching travel recommendations.

## Features
- Extracts and refines user-provided travel details.
- Fetches **real-time travel recommendations** using Google Search API.
- Generates a **structured, personalized itinerary** based on user preferences.
- Hosted on **Streamlit** for easy user interaction.

## Tech Stack
- **Python**
- **Streamlit** (for UI)
- **OpenAI API** (for AI-powered responses)
- **Google Search API** (for travel recommendations)
- **Requests, dotenv** (for API calls & environment management)

## Installation
### Prerequisites
Ensure you have Python installed. Install dependencies using:
```bash
pip install streamlit openai requests python-dotenv
```

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-travel-planner.git
   cd ai-travel-planner
   ```
2. Create a **.env** file and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## How It Works
### 1. User Input Processing
- Users enter their trip details in a text box.
- The AI refines the input and ensures key details are captured (budget, destination, duration, etc.).

### 2. Travel Recommendations
- The app fetches **real-time travel recommendations** using Google Search API.
- Results are structured and displayed in JSON format.

### 3. Itinerary Generation
- The AI processes the refined input and generates a **day-by-day itinerary** with:
  - Grouped activities
  - Time slots
  - Meals & breaks
- The itinerary is displayed in a structured format.

## Example Usage
- **User Input:** "I want a luxury trip to Paris for 5 days with a focus on food and art."
- **Refined Output:** Extracted key details and preferences.
- **Recommendations:** Top Paris attractions for food and art lovers.
- **Generated Itinerary:** Day-wise structured plan.

## Deployment
deploy the app on **Streamlit Cloud**
