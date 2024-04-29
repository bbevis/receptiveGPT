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
    topic = "The United States should invest greater economic, military, and human resources in helping Ukraine fight Russia."
    opposing_view = "I do not think that the US should invest more into their military. They already have the largest budget in NATO by far. There is no evidence to suggest that more investment leads to a higher likelihood of peace. In fact, it's likely to lead to more conflict in my opinion. It is best to stay out of other people’s war."
    writer_statement = "we should always those in need. It is the role of the US!"

    prompt = pg.get_prompt("recipe", writer_statement, opposing_view, topic)
    response = chat_gpt(prompt = prompt,
                        context = "You are a human writer attepting to discuss a controversial issue with someone with an opposing view")
    
    print('')
    print(prompt)
    print('')
    print(response)
