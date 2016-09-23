from flask import Flask, render_template, request, url_for, make_response, jsonify, session, redirect, g, flash
import random, urllib
from dogeify import *
from quotes import *
import dogeconfig
import nltk.data, nltk.tag

tagger = nltk.data.load("taggers/maxent_treebank_pos_tagger/english.pickle")

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    getMode = False
    return render_template("home.html", getMode=getMode, result=[])    

@app.route("/dogeify", methods=['GET', 'POST'])
def dogeifyText():
    text = ""
    if request.method == "GET":
        text = request.args.get("userText")
    else:
        text = request.form['userText']

    if len(text) > 2000:
        errormsg = colorify(["such error."])
        return render_template("home.html", getMode=True, result=["such error.", errormsg])

    dogeTextArray = dogeify(text, tagger)
    dogeResult = colorify(dogeTextArray)
    result = [text, dogeResult]

    if request.method == "GET":
        return render_template("home.html", getMode=True, result=result)
    elif request.method == "POST":
        return jsonify(list=result)

@app.route("/lucky")
def lucky():
    quote = random.choice(quotes)
    return redirect("/dogeify?userText="+urllib.quote_plus(quote))


if __name__ == '__main__':
    app.run(host=dogeconfig.host, port=dogeconfig.port, debug=dogeconfig.debug)
