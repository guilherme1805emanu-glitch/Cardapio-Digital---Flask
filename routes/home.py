from flask import Blueprint, render_template

app_home = Blueprint('home', __name__)

@app_home.route('/')
def route_home():
    return render_template("home.html")
