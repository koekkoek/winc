import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if not username and not password:
            error_msg = "Please enter a username and password"
            return render_template("login.html", error=True, error_msg=error_msg)
        elif not username:
            error_msg = "Please enter a username"
            return render_template("login.html", error=True, error_msg=error_msg)
        elif not password:
            error_msg = "Please enter a password"
            return render_template("login.html", error=True, error_msg=error_msg)
        password = hash_password(password)
        users = get_users()
        for usern, passw in users.items():
            if username == usern:
                if password == passw:
                    session["username"] = username
                    return redirect(url_for("dashboard"))
    else:
        return render_template("login.html")


@app.route("/login?error=<error>")
def error(error):
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if not session.get("username"):
        return redirect("/login")
    return render_template("dashboard.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if session.get("username"):
        session.pop('username')
    return render_template("index.html")
