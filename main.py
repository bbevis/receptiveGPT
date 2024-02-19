import openai
import requests
import json
import os
import config

OPENAI_API_KEY = config.api_key

if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key is not detected. Consider setting API key in environment variables.")


openai.api_key = OPENAI_API_KEY

def chat_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content": "You are a the Queen of England"}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    response = chat_gpt("write a very short political manifesto")
    print(response)
