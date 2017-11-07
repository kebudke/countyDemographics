from flask import Flask, url_for, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/")
def render_home():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('home.html',options=get_state_options(counties))

def get_state_options():
    states = []
    for s in counties:
        if s["State"] not in states:
            states.append[s["State"]]
        options=""
    for o in states:
        options += Markup("<option value=\"" + o + "\">" + o + "</option>")
    return options

if __name__=="__main__":
    app.run(debug=False, port=54321)

    
