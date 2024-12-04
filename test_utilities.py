# test_utilities.py
import os
from dotenv import load_dotenv
import utilities as U

# Load environment variables
load_dotenv()
# Test the utility
prompt = "What is the meaning of life?"
response = U.generate_response_with_gemini(prompt)
print("Response:", response)