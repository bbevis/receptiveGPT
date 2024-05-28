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
    topic = "Hamas bears a lot of responsibility for the current conflict than the Israeli government"
    opposing_view = """Hamas is the real problem, not Israel. Hamas's terrorism, rocket attacks, and use of human shields drive the conflict.
    Their relentless violence and refusal to recognize Israel’s right to exist perpetuate the bloodshed.
    Blaming Israel ignores the reality of Hamas's aggression and extremism."""
    writer_statement = "we should always help everyone"

    prompt = pg.get_prompt("baseline", writer_statement, opposing_view, topic)
    response = chat_gpt(prompt = prompt,
                        context = "You are a human writer attepting to discuss a controversial issue with someone with an opposing view")
    
    print('')
    print(prompt)
    print('')
    print(response)
