from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/entry")
def entry():
    return render_template('entry.html')

@app.route("/_entry")
def edit_entry():
    return render_template('_entry.html')


if __name__ == "__main__":
    app.run(debug=True)