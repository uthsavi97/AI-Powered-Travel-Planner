# AI/ML Internship Assignment - AI-Powered Travel Planner

## Objective
The goal of this assignment is to build an AI agent system that assists travelers by providing personalized travel plans and recommendations. The system should simulate a conversation to gather user preferences, curate relevant suggestions via web search, and generate a structured travel itinerary.

## Scenario
You are developing an AI-powered travel planner that provides users with customized travel itineraries. Your task is to:
- Prototype an AI-agentic system for this use case.
- Develop prompts to facilitate user interactions.
- Use a web-search tool to curate recommendations.
- Generate a detailed travel itinerary.
- Deploy your solution using a free hosting provider like Streamlit or Gradio.

---

## Task Instructions
### **Step 1: Understand the User Context**
1. Analyze user messages for key inputs:
   - **Budget**
   - **Trip Duration or Travel Dates**
   - **Destination & Starting Location**
   - **Purpose of Travel**
   - **Preferences (e.g., adventure, relaxation, cultural, food, etc.)**
2. Extract key details and:
   - Chain prompts effectively to refine missing or unclear inputs.
   - Generate a structured, day-by-day itinerary.

### **Step 2: Build Your Prompt System**
1. **Input Refinement:**
   - Create a system prompt to clarify user inputs such as:
     - Dietary preferences.
     - Specific interests.
     - Walking tolerance or mobility concerns.
     - Accommodation preferences (luxury, budget, central location, etc.).
2. **Activity Suggestions:**
   - Use a web-search tool to:
     - Generate up-to-date recommendations for attractions, dining, and activities.
     - Align suggestions with user preferences (e.g., “Hidden Gems”).
3. **Itinerary Generation:**
   - Once user preferences are confirmed, generate a structured multi-day itinerary with:
     - Logical grouping and timing of sightseeing and activities.
     - Recommendations for meals, transportation, and accommodations.

### **Step 3: Deliverables**
- Submit the final set of prompts used, categorized as:
  - **System Prompt** (instructions given to the AI model)
  - **User Prompt** (sample user inputs)
  - **Model Response** (AI-generated output)
- Provide sample inputs and outputs:
  - A set of curated travel suggestions based on user inputs.
  - A detailed, structured itinerary for a provided user scenario.
- Document the reasoning behind each prompt and response strategy.
- Host the application on a free hosting service (e.g., Streamlit, Gradio) and submit the live application link.

---

## **Bonus Challenge (Optional)**
Enhance the itinerary generation process by incorporating:
- Flexible input handling (e.g., interpreting vague user preferences like "I have a moderate budget and want a mix of famous and offbeat places").
- Intelligent prompt refinement to request clarifications when user inputs are incomplete or ambiguous.

---

## **Evaluation Criteria**
1. **Prompt Design:**
   - Are prompts clear, structured, and effective?
   - Do they ensure meaningful and relevant AI responses?
2. **Prompt Chaining:**
   - Are prompts strategically structured to refine user inputs?
   - Do they maintain a logical conversation flow?
3. **Personalization:**
   - How well does the output align with user preferences?
   - Is the itinerary unique and relevant to the user?
4. **Documentation:**
   - Is the thought process well-documented and explained?

---

## **Estimated Time Commitment**
- **Prompt Design & Testing:** 3-4 hours
- **AI Agent Development:** 3-4 hours
- **Hosting Deployment:** 1-2 hours
- **Documentation:** <1 hour

---

## **Submission Guidelines**
- Share the **final prompt set**, **sample outputs**, and **documentation**.
- Provide a **live application link** for testing.
- Ensure clear and structured documentation for evaluation.

Good luck and happy coding!

