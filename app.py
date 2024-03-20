from flask import Flask, request, jsonify, render_template, flash
from flask import redirect, url_for, send_from_directory, send_file, Response
import os
import pandas as pd
import numpy as np
import api
import prompt as pg

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # limit files sizes to 16 MBs. Flask will raise a RequestEntityTooLarge exception.
app.secret_key = '514609ea9026b3956660d714'

#--- ROUTES ---#
@app.route('/')
def home():
	return render_template('index.html')
 
@app.route('/paraphrase', methods=['GET','POST'])
def paraphrase():
    
    topic = "The US should introdce stronger regulations on guns. For example, automatic rifles should be banned."
    opposing_view = "It's our second amendment rights! We can't let these liberals take away our guns!"
    
    writer_statement = request.form['text']
    
    prompt = pg.get_prompt("recipe", writer_statement, opposing_view, topic)
    response = api.chat_gpt(prompt = prompt,
                        context = "You are a helpful writing assistant")
    
    flash(response)
    return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)