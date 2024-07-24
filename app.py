from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def welcome():
    return "First flask program"

@app.route("/home")
def home():
    return "This is home page"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template(login.html)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

from controller import user_controller, product_controller