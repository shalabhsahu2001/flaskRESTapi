from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "First flask program"

@app.route("/home")
def home():
    return "This is home page"

from controller import user_controller, product_controller