from flask import Flask, render_template, redirect, request
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "GET":
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)

        return render_template("index.html", R = R, G = G, B = B)

    
if __name__ == "__main__":
    app.run()