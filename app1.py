import ast
from bestcode import create
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/create",methods=["GET","POST"])
def create():
	return render_template("create.html")

@app.route("/created",methods=["GET","POST"])
def created():
	create()
	return render_template("created.html", msg="Topic Created")

@app.route("/explore",methods=["GET","POST"])
	def explore():
	return render_template("Explore.html")


if __name__  == "__main__":
	app.run(debug = True)