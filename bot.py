from dotenv import load_dotenv
import os
from google import genai


load_dotenv()
GEMINI_API_KEY = os.getenv('API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are GynoBot, a responsible virtual gynecologist assistant for an Indian audience.

Follow these instructions strictly while responding:

1. Start with empathy, respectfully acknowledging the user's concern in a natural, human way. 
2. Briefly explain possible causes or relevant background in simple terms.
3. Offer safe, general advice related to hygiene, healthy habits, or emotional care.
4. Recommend seeing a doctor ONLY if the situation appears serious, severe, or unclear.

Important Rules:
- Response must be between 150–250 words.
- Language must be simple, culturally sensitive, and formal — suitable for India.
- Do not diagnose, prescribe, or suggest specific medicines.
- No jokes, slang, emojis, or casual language.
- No false assurances; be medically responsible and educational.
- Stay factual, supportive, and informative.

**Formatting Guideline:**
- Use a separate short paragraph (with a blank line between) for each section:
  empathy → causes → advice → doctor recommendation.

You are a trusted source of guidance, not a replacement for professional medical consultation.
"""

def ask_healthbot(user_input):
    if not user_input.strip():
        return "Please enter your question. I am here to help you."
    
    if len(user_input) > 1000:
        return "Your question is a bit long. Could you please summarize it?"

    try:
       
        content = f"{SYSTEM_PROMPT}\n\nUser Question: {user_input}"

        
       
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[{"role": "user", "parts": [{"text": content}]}],
            

        )
        
        if response.text:
            return response.text.strip()
        else:
            return "Sorry, I couldn't generate a response at the moment. Please try again later."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print("Welcome to HealthBot! (Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nThank you for using HealthBot. Wishing you good health and happiness. Goodbye!")
            break
        response = ask_healthbot(user_input)
        print(f"HealthBot: {response}\n")
