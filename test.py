import os
import pandas as pd
import numpy as np
import main
import prompt_generate as pg

df = pd.read_csv('edit2Braw.csv')

df = df[['issuetext', 'seedtext', 'message1']].dropna().sample(20)

suggestions_baseline = []
suggestions_recipe = []
suggestions_words = []


for i in range(len(df)):
    
    out1 = main.chat_gpt(prompt = pg.get_prompt("baseline", df['message1'].iloc[i], df['seedtext'].iloc[i], df['issuetext'].iloc[i]),
                            context = "You are a helpful writing assistant")
    out2 = main.chat_gpt(prompt = pg.get_prompt("recipe", df['message1'].iloc[i], df['seedtext'].iloc[i], df['issuetext'].iloc[i]),
                            context = "You are a helpful writing assistant")
    out3 = main.chat_gpt(prompt = pg.get_prompt("words", df['message1'].iloc[i], df['seedtext'].iloc[i], df['issuetext'].iloc[i]),
                            context = "You are a helpful writing assistant")
    suggestions_baseline.append(out1)
    suggestions_recipe.append(out2)
    suggestions_words.append(out3)
    
    
df['suggestions_baselines'] = suggestions_baseline
df['suggestions_recipe'] = suggestions_recipe
df['suggestions_words'] = suggestions_words

df.to_csv('gpt_outputs.csv')