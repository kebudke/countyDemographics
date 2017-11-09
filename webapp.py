from flask import Flask, request, Markup, render_template, flash, Markup
import json
import os

app = Flask(__name__)

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    states = []
    for s in counties:
        if s["State"] not in states:
            states.append(s["State"])
    options = ""
    for o in states:
        options += Markup("<option value=\"" + o + "\">" + o + "</option>")
    return options

def get_fun_fact():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    education = {}
    
    return fact

@app.route("/")
def render_main():
    return render_template('home.html', options = get_state_options())

if __name__=="__main__":
    app.run(debug=False, port=54321)

    
