from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

def get_state_options(counties):
    for state in counties:
        
    options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
