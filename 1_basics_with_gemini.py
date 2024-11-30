from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Configure the API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# api_key = os.getenv('GOOGLE_API_KEY')
# Print the API key
# print(f"API Key: {api_key}")
#instantiate the model
model=genai.GenerativeModel('gemini-pro')
answer= model.generate_content('How many models are there in Google Gemini, also name them ,give me the parameter detaisl as well')
# Hallucination
print(answer.text)



