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

def get_fun_fact(state):
    fact = state
    return fact

@app.route("/")
def render_main():
    if 'state' in request.args['state']:
        return render_template('home.html', options = get_state_options(), funfact = get_fun_fact(request.args['state']))
    else:
        return render_template('home.html', options = get_state_options())

if __name__=="__main__":
    app.run(debug=False, port=54321)

    
