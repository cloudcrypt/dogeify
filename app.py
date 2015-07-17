from flask import Flask, render_template, request, url_for, make_response, session, redirect, g, flash
from dogeify import *
from colors import *
import random


app = Flask(__name__)
# app.config.from_object(__name__)
#app.secret_key = '\xdc\xae\xd5\xce\x9a\x83\x8d\xe1\x0e\xe7K>\xc5O\x18\xa0\r6\x87=\xf8\xe3<\x88'




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
    return render_template("dogetext.html", result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
