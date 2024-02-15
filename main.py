import openai
import requests
import json
import os

API_KEY = open("API_KEY", "r").read()
if API_KEY is None:
    raise ValueError("OpenAI API key is not set in environment variables.")


openai.api_key = API_KEY

def chat_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_gpt(user_input)
        print("Bot:", response)