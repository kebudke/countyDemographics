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
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    totalpop = {}
    popwithb = {}
    for s in counties:
        if s["State"] in totalpop:
            totalpop[s["State"]] = totalpop[s["State"]] + s["Population"]["2014 Population"]
        else:
            totalpop[s["State"]] = s["Population"]["2014 Population"]
#     for b in counties:
#         if s["State"] in popwithb:
#             popwithb[s["State"]] = popwithb[s["State"]] + s["Population"]["2014 Population"]
#         else:
#             popwithb[s["State"]] = s["Population"]["2014 Population"]
    return fact

@app.route("/")
def render_main():
    if 'state' in request.args:
        return render_template('home.html', options = get_state_options(), funfact = get_fun_fact(request.args['state']))
    else:
        return render_template('home.html', options = get_state_options())

if __name__=="__main__":
    app.run(debug=True)

    
