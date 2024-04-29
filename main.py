from flask import Flask, request, jsonify, render_template, flash
from flask import redirect, url_for, send_from_directory, send_file, Response
import os
import pandas as pd
import numpy as np
import api
import prompt as pg
import json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # limit files sizes to 16 MBs. Flask will raise a RequestEntityTooLarge exception.
app.secret_key = '514609' # this is just a random number

#--- ROUTES ---#
 
@app.route('/', methods=['GET','POST'])
def paraphrase():
    
    topic = "The United States should invest greater economic, military, and human resources in helping Ukraine fight Russia."
    opposing_view = "I do not think that the US should invest more into their military. They already have the largest budget in NATO by far. There is no evidence to suggest that more investment leads to a higher likelihood of peace. In fact, it's likely to lead to more conflict in my opinion. It is best to stay out of other people’s war."
    
    # writer_statement = request.form['text']
    writer_statement = request.args.get('text', None)
    
    prompt = pg.get_prompt("baseline", writer_statement, opposing_view, topic)
    response = api.chat_gpt(prompt = prompt,
                        context = "You are a human writer attepting to discuss a controversial issue with someone with an opposing view")
    
    jsondata = json.dumps(
        {
            "suggestion": response
        })
    
    return jsondata

if __name__ == "__main__":
	app.run(debug=True)