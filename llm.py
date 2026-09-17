import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")

def generate_reply(prompt):
    response = model.generate_content(prompt)
    return response.text