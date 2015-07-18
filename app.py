from flask import Flask, render_template, request, url_for, make_response, jsonify, session, redirect, g, flash
import random, urllib
from dogeify import *
from colors import *


app = Flask(__name__)
# app.config.from_object(__name__)
app.secret_key = '\xa6e\x93\xaf\xb4\xfax\xcc4\x8cB\xb6m\xce\x80\xdcu~\xa7|\xa6\xadQ\xd9'




@app.route("/")
def index():
    return render_template("home.html")

@app.route("/dogeify", methods=['GET', 'POST'])
def dogeifyText():
    if request.method == "GET":
        text = request.args.get("userText")
    else:
        text = request.form['userText']
    if len(text) > 2000:
        flash("Text has exceeded length limit!")
        return render_template("home.html", flashType="danger")  
    dogeTextArray = superdogeify(text)
    dogeResult = []
    for dogePair in dogeTextArray:
        dogeResult.append([dogePair, random.choice(htmlColors.keys())])
    result = [text, dogeResult]
    processHistory(text)
    if request.method == "GET":
        return render_template("dogetext.html", result=result)
    elif request.method == "POST":
        return jsonify(list=result)
            
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
    app.run(host='0.0.0.0', debug=True)
