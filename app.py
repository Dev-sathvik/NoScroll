import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import lookup, login_required
from datetime import *


# Configure application
app = Flask(__name__)
app.secret_key = 'a_very_long_random_string'


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///noscroll.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    rows = db.execute("SELECT *  FROM enrolled")
    return render_template("index.html", rows=rows)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Please provide Username")
            return render_template("login.html")
            #return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Please provide Password")
            return render_template("login.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
                flash("Please provide valid Username or Password")
                return render_template("login.html")


        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        # display registration form
        return render_template("register.html")

    elif request.method == "POST":
        # Check for possible errors and insert new user to users table. Also login directly
        name = request.form.get("username")
        pass1 = request.form.get("password")
        pass2 = request.form.get("confirmation")

        if not name:
            flash("Must provide Username")
            return render_template("register.html")

        if not pass1 or not pass2:
            flash("Must provide Password")
            return render_template("register.html")

        if pass1 != pass2:
            flash("Password are distinct")
            return render_template("register.html")

        row = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(row) != 0:
            flash("Username already present")
            return render_template("register.html")

        password = generate_password_hash(pass1)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, password)

        result = db.execute("SELECT id FROM users WHERE username = ?", name)
        session["user_id"] = result[0]["id"]

        return redirect("/")

@app.route("/enroll", methods=["GET", "POST"])
@login_required
def enroll():
    user_id = session.get("user_id")
    if request.method == "GET":
        user_id = session.get("user_id")
        enrolled_name = db.execute("SELECT name FROM enrolled where id = ?", user_id)
        if len(enrolled_name) == 0:
            return render_template("enroll.html", flag=True)
        else:
            motivation = lookup()
            print(motivation)
            return render_template("enroll.html", flag=False, motivation=motivation)

    elif request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        motivation = request.form.get("motivation")
        timespan = request.form.get("time")

        if not name or not username or not motivation or not timespan:
            flash("Please enter all fields")
            return render_template("enroll.html" ,flag=True)
            #display error
        print(name,username,motivation)
        cur_date = date.today()
        db.execute("INSERT INTO enrolled (id, name, username, motivation, enroll_date, time) VALUES (?, ?, ?, ?, ?, ?)",user_id, name, username, motivation, cur_date, timespan)
        motivation = lookup()
        print(motivation)
        return render_template("enroll.html", flag=False, motivation=motivation)

@app.route("/exit", methods=["POST"])
@login_required
def exit():
    # Handle the exit action here
    user_id = session.get("user_id")
    db.execute("DELETE FROM enrolled where id = ?", user_id)
    return redirect("/")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "GET":
        user_id = session.get("user_id")
        streak = 0
        time_saved = 0
        rows = db.execute("SELECT *  FROM enrolled where id = ?", user_id)
        if len(rows) != 0:
            enrollment_date = datetime.strptime(rows[0]["enroll_date"], "%Y-%m-%d")
            today = datetime.today()
            streak = (today - enrollment_date).days
            time_saved = streak * rows[0]["time"]
        return render_template("profile.html", rows=rows, streak=streak, time_saved=time_saved)



@app.route("/stats", methods=["GET"])
@login_required
def stats():
    users = db.execute("SELECT COUNT(id) FROM users")
    enrolled = db.execute("SELECT COUNT(id) FROM enrolled")
    today = db.execute("SELECT COUNT(id) FROM enrolled WHERE enroll_date = DATE('now')")
    today = today[0]["COUNT(id)"]
    print(today)
    return render_template("stats.html", users = users[0]["COUNT(id)"], enrolled = enrolled[0]["COUNT(id)"], today = today)




