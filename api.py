import openai
import requests
import json
import os
import config
import prompt as pg

OPENAI_API_KEY = config.api_key

if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key is not detected. Consider setting API key in environment variables.")


openai.api_key = OPENAI_API_KEY

def chat_gpt(prompt, context):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content": context}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    topic = "The US should introdce stronger regulations on guns. For example, automatic rifles should be banned."
    opposing_view = "It's our second amendment rights! We can't let these liberals take away our guns!"
    writer_statement = "Evidence from around the world suggests gun regulations work. Read a book you idiot!"
    prompt = pg.get_prompt("recipe", writer_statement, opposing_view, topic)
    response = chat_gpt(prompt = prompt,
                        context = "You are a helpful writing assistant")
    
    print('')
    print(prompt)
    print('')
    print(response)
