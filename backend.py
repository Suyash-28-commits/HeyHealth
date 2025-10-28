import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)

def chatbot(user_input):
    response = model.generate_content([
  ""
  "input: who are you",
  "output: i am a healthcare chatbot",
  "input: What all can you do?", 
  "output: I can provide details about the diseases you might be suffering from according to the symptoms specified",
  f"input: {user_input}",
  "output: ",
])
    return response.text

# while True:
#     string = str(input("Enter your prompt: "))
#     print("Bot: ",chatbot(string))