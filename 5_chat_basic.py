from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

chat= model.start_chat(history=[]) #set the history parameter as empty list here

answer = chat.send_message("give a short description on the difference of east coast and west coast weather")

## chat history is stores as list of special object knows as parts
print(type(chat.history))

# note the role here is user
# chat.history[0]

# note the role here is model
# chat.history[1]

# Extract the text
chat.history[1].parts[0].text

answer= chat.send_message('Can you be a little more specific')

# answer.text

answer= chat.send_message('Tell me about the questions I have asked till now')

# answer.text

answer= chat.send_message('What have I asked you so far, be very specific on the answer')

print(answer.text)

for item in chat.history:
    print(f'{item.role.capitalize()}:{item.parts[0].text}')
    print('__'* 100)
