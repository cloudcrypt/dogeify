from flask import Flask, render_template, request, url_for, make_response, jsonify, session, redirect, g, flash
import random, urllib
from dogeify import *
from colors import *
import dogeconfig

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
        errormsg = [["such error.", random.choice(htmlColors.keys())]]
        return render_template("home.html", getMode=True, result=[text, errormsg])
    dogeTextArray = dogeify(text)
    dogeResult = []
    for dogePair in dogeTextArray:
        dogeResult.append([dogePair, random.choice(htmlColors.keys())])
    result = [text, dogeResult]
    if request.method == "GET":
        getMode = True
        return render_template("home.html", getMode=getMode, result=result)
    elif request.method == "POST":
        return jsonify(list=result)
            
if __name__ == '__main__':
    app.run(host=dogeconfig.host, port=dogeconfig.port, debug=dogeconfig.debug)
