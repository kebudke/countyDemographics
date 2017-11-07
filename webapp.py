from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__)

def get_state_options(counties):
    states = []
    for s in counties:
        if s["State"] not in states:
            states.append[s["State"]]
        options=str("")
    for o in states:
        options += Markup("<option value=\"" + states[o] + "\">" + states[o] + "</option>")
    return options
    
@app.route("/")
def render_main():
    return render_template('home.html',options=get_state_options(counties))
    
if __name__=="__main__":
    app.run(debug=False, port=54321)

    
