from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

prompt = 'Write a long essay on Indian cricket teams Gabba test win'

answer = model.generate_content(prompt, stream=True)

for chunk in answer:
    print(chunk.text)