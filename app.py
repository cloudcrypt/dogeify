from flask import Flask, render_template, request, url_for, make_response, session, redirect, g, flash
import random, urllib
from dogeify import *
from colors import *


app = Flask(__name__)
# app.config.from_object(__name__)
app.secret_key = '\xa6e\x93\xaf\xb4\xfax\xcc4\x8cB\xb6m\xce\x80\xdcu~\xa7|\xa6\xadQ\xd9'




@app.route("/")
def index():
    return render_template("home.html")

@app.route("/dogeify", methods=['GET'])
def dogeifyText():
    text = request.args.get("userText")
    dogeTextArray = superdogeify(text)
    dogeResult = []
    for dogePair in dogeTextArray:
        dogeResult.append([dogePair, random.choice(htmlColors.keys())])
    result = [text, dogeResult]
    #processHistory(text)
    return render_template("dogetext.html", result=result)
    
@app.route('/clearhistory')
def clearHistory():
    session.pop('history')
    flash("History has been cleared.")
    return render_template("home.html", flashType="success")    

def processHistory(set):
    historyPair = [set, urllib.quote_plus(set)]
    if 'history' not in session:
        session['history'] = []
    if historyPair in session['history']:
        return
    else:
        session['history'].append(historyPair)
        return

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
