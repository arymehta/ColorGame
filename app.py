from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")

    

