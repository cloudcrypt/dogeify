from flask import Flask, render_template, request, url_for, make_response, session, redirect, g, flash
import random, urllib
from dogeify import *
from colors import *
import dogeconfig

app = Flask(__name__)
# app.config.from_object(__name__)
app.secret_key = dogeconfig.secret_key




@app.route("/")
def index():
    return render_template("home.html")

@app.route("/dogeify", methods=['GET'])
def dogeifyText():
    text = request.args.get("userText")
    if len(text) > 2000:
        flash("Text has exceeded length limit!")
        return render_template("home.html", flashType="danger")  
    dogeTextArray = superdogeify(text)
    dogeResult = []
    for dogePair in dogeTextArray:
        dogeResult.append([dogePair, random.choice(htmlColors.keys())])
    result = [text, dogeResult]
    processHistory(text)
    return render_template("dogetext.html", result=result)
    
@app.route('/clearhistory')
def clearHistory():
    session.pop('history')
    flash("History has been cleared.")
    return render_template("home.html", flashType="success")    

def processHistory(set):
    if len(set) > 150:
        return
    historyPair = [set, urllib.quote_plus(set.encode('ascii', 'ignore'))]
    if 'history' not in session:
        session['history'] = []
    if historyPair in session['history']:
        return
    else:
        session['history'].append(historyPair)
        return

if __name__ == '__main__':
    app.run(host=dogeconfig.host, port=dogeconfig.port, debug=True)
