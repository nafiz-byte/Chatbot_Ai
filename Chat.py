from http.client import responses

import google.generativeai as Nafiz
API_KEY = "AIzaSyA13N964-zXpSoc1IB-1qzVpcD5PieTbr8"

Nafiz.configure(api_key=API_KEY)

model = Nafiz.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat()

print("Welcome to Nafiz-intelligence!!")

while True:
    user_input = input("You: ")
    if user_input.lower() =="exit":
        break
    responses = chat.send_message(user_input)
    print("Nafiz: ",responses.text)