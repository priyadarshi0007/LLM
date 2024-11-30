from dotenv import load_dotenv
import os
import google.generativeai as genai
import PIL.Image
import base64
import httpx


load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel(model_name = "gemini-1.5-pro")
image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/2560px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg"
image = httpx.get(image_path)

image_path = '/Users/priyadarshisoumyakumar/Downloads/LLMVSCode/BasicLLM/test_img.jpeg'
sample_file_1 = PIL.Image.open(image_path)

prompt = "Caption this image."
answer = model.generate_content([{'mime_type':'image/jpeg', 'data': base64.b64encode(image.content).decode('utf-8')}, prompt])

prompt = "Write whats happening in the image"

response = model.generate_content([prompt, sample_file_1])

print(answer.text)
print("****************************************")
print(response.text)
