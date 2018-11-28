import ast
from bestcode import create
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/loggedin",methods=["GET","POST"])
def loggedin():
	return render_template("loggedin.html")


if __name__  == "__main__":
	app.run(debug = True)