import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import datetime, timezone

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///data.db")


level = 1
# for storing the levels.

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/solve")
def check():
    global level
    if level == 1:
        return render_template("q1.html")
    elif level == 2:
        return render_template("q2.html")
    elif level == 3:
        return render_template("q3.html")
    elif level == 4:
        return render_template("q4.html")
    elif level == 5:
        return render_template("q5.html")
    elif level == 6:
        return render_template("q6.html")
    elif level == 7:
        return render_template("q7.html")
    elif level == 8:
        return render_template("q8.html")
    elif level == 9:
        return render_template("q9.html")
    elif level == 10:
        return render_template("q10.html")
    else:
        return render_template("complete.html")


@app.route("/start", methods=["GET", "POST"])
def start():

    if request.method == "POST":
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/complete", methods=["GET", "POST"])
def complete():
    restart_level = 1
    if request.method == "POST":
        id = session["user_id"]
        db.execute("UPDATE users SET level = ? WHERE id = ?", restart_level, id)
        return render_template("index.html")
    else:
        return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    lev = 1
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if password != confirmation:
            return render_template("match.html")

        hash = generate_password_hash(password)
        user = db.execute("SELECT username FROM users WHERE username =?", username)
        if not user:
            db.execute(
                "INSERT INTO users (username, hash, level) VALUES (?, ?, ?)", username, hash, lev
                )
            return render_template("login.html")
        else:
            return render_template("user.html")
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    global level
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("password.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        level = db.execute("SELECT level FROM users WHERE id = ?", session["user_id"])[0]["level"]
        return redirect("/solve")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    global level
    # Remember which user has logged in
    id = session["user_id"]

    db.execute("UPDATE users SET level = ? WHERE id = ?", level, id)
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return render_template("login.html")


@app.route("/q1", methods=["GET", "POST"])
def q():
    global level
    if request.method == "POST":
        answer = request.form.get("answer")
        an = answer.upper()

        if an == "COAL":
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q1.html")
    else:
        return render_template("q1.html")


@app.route("/q2", methods=["GET", "POST"])
def q2():
    global level
    if request.method == "GET":
        return render_template("q2.html")
    else:
        answer = request.form.get("answer")
        try:
            answer = int(answer)
        except:
            return render_template("q2.html")

        if answer == 1:
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q2.html")


@app.route("/q3", methods=["GET", "POST"])
def q3():
    global level
    if request.method == "GET":
        return render_template("q3.html")
    else:
        answer = request.form.get("answer")
        try:
            answer = int(answer)
        except:
            return render_template("q3.html")

        if answer == 16:
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q3.html")


@app.route("/q4", methods=["GET", "POST"])
def q4():
    global level
    if request.method == "GET":
        return render_template("q4.html")
    else:
        answer = request.form.get("answer")
        answer = answer.upper()

        if answer == "DAVID":
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q4.html")


@app.route("/q5", methods=["GET", "POST"])
def q5():
    global level
    if request.method == "GET":
        return render_template("q5.html")
    else:
        answer = request.form.get("answer")
        answer = answer.upper()

        if answer == "LIBRARY":
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q5.html")


@app.route("/q6", methods=["GET", "POST"])
def q6():
    global level
    if request.method == "GET":
        return render_template("q6.html")
    else:
        answer = request.form.get("answer")
        answer = answer.upper()

        if answer == "TEA":
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q6.html")


@app.route("/q7", methods=["GET", "POST"])
def q7():
    global level
    if request.method == "GET":
        return render_template("q7.html")
    else:
        answer = request.form.get("answer")
        answer = answer.upper()

        if answer == "SPONG":
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q7.html")


@app.route("/q8", methods=["GET", "POST"])
def q8():
    global level
    if request.method == "GET":
        return render_template("q8.html")
    else:
        answer = request.form.get("answer")
        try:
            answer = int(answer)
        except:
            return render_template("q8.html")

        if answer == 8:
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q8.html")


@app.route("/q9", methods=["GET", "POST"])
def q9():
    global level
    if request.method == "GET":
        return render_template("q9.html")
    else:
        answer = request.form.get("answer")
        try:
            answer = int(answer)
        except:
            return render_template("q9.html")
        if answer == 6:
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q9.html")


@app.route("/q10", methods=["GET", "POST"])
def q10():
    global level
    if request.method == "GET":
        return render_template("q10.html")
    else:
        answer = request.form.get("answer")
        answer = answer.upper()

        if answer == "SNAKE":
            level += 1
            return render_template("correct.html")
        else:
            return render_template("q10.html")
