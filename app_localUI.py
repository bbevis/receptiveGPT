from flask import Flask, request, jsonify, render_template, flash
from flask import redirect, url_for, send_from_directory, send_file, Response
import os
import pandas as pd
import numpy as np
import api
import prompt as pg

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # limit files sizes to 16 MBs. Flask will raise a RequestEntityTooLarge exception.
# app.secret_key = '514609ea9026b3956660d714'

app.secret_key = '514609'

#--- ROUTES ---#
@app.route('/')
def home():
	return render_template('index.html')
 
@app.route('/paraphrase', methods=['GET','POST'])
def paraphrase():
    
    topic = "Hamas bears a lot of responsibility for the current conflict than the Israeli government"
    opposing_view = """Hamas is the real problem, not Israel. Hamas's terrorism, rocket attacks, and use of human shields drive the conflict.
    Their relentless violence and refusal to recognize Israel’s right to exist perpetuate the bloodshed.
    Blaming Israel ignores the reality of Hamas's aggression and extremism."""
    
    writer_statement = request.form['text']
    
    prompt = pg.get_prompt("baseline", writer_statement, opposing_view, topic)
    response = api.chat_gpt(prompt = prompt,
                        context = "You are a human writer attepting to discuss a controversial issue with someone with an opposing view")
    
    flash(response)
    return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)