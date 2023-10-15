import os
import cs50
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def info():
    return render_template("info.html")

@app.route("/index.html", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        code = request.form.get("finalcode")
        if code == "PLXAT":
            return render_template("security_questions.html")
        else:
            return render_template("index.html")

@app.route("/p1.html")
def p1():
    return render_template("p1.html")

@app.route("/p2.html")
def p2():
    return render_template("p2.html")

@app.route("/p3.html")
def p3():
    return render_template("p3.html")

@app.route("/p4.html")
def p4():
    return render_template("p4.html")

@app.route("/p5.html")
def p5():
    return render_template("p5.html")

@app.route("/p6.html")
def p6():
    return render_template("p6.html")

@app.route("/p7.html")
def p7():
    return render_template("p7.html")

@app.route("/p8.html")
def p8():
    return render_template("p8.html")

@app.route("/p9_last.html")
def p9():
    return render_template("p9_last.html")

@app.route("/hint.html")
def hint():
    return render_template("hint.html")

@app.route("/password1.html", methods=["GET", "POST"])
def password():
    if request.method == "GET":
        return render_template("password1.html")
    if request.method == "POST":
        password = request.form.get("password")
        if password == "#11348":
            return render_template("enter_password.html")
        else:
            return render_template("password1.html")


@app.route("/puzzle2.html", methods=["GET", "POST"])
def puzzle2():
    if request.method == "GET":
        return render_template("puzzle2.html")

    if request.method == "POST":
        name = request.form.get("name")
        cord = request.form.get("coordinates")
        date = request.form.get("date")
        if name == "LOUVRE" or "THE LOUVRE" and cord == "PARIS" or "FRANCE" and date == "10/08/1793":
            return render_template("puzzle2_p2.html")
        else:
            return render_template("puzzle2.html")

@app.route("/puzzle2_p2.html")
def puzz2p2():
    return render_template("puzzle2_p2.html")

@app.route("/ransom.html", methods=["GET", "POST"])
def ransom():
    if request.method == "GET":
        return render_template("ransom.html")
    if request.method == "POST":
        ransom = request.form.get("ransom")
        if ransom == "SLIP UP AND THEY DIE":
            return render_template("ransom2.html")
        else:
            return render_template("ransom.html")

@app.route("/ransom2.html")
def ransom2():
    return render_template("ransom2.html")

@app.route("/slider.html", methods=["GET", "POST"])
def slider():
    if request.method == "GET":
        return render_template("slider.html")
    if request.method == "POST":
        slider1 = int(request.form.get("slide1"))
        slider2 = int(request.form.get("slide2"))
        slider3 = int(request.form.get("slide3"))
        slider4 = int(request.form.get("slide4"))
        if (slider1 > 35 and slider1 < 45) and (slider2 > 25 and slider2 < 35) and (slider3 > 85) and (slider4 > 55 and slider4 < 65):
            return render_template("slider2.html")
        else:
            return render_template("slider.html")

@app.route("/security_questions.html", methods=["GET", "POST"])
def questions():
    if request.method == "GET":
        return render_template("security_questions.html")
    if request.method == "POST":
        pet = request.form.get("pet")
        marry = request.form.get("marry")
        color = request.form.get("color")
        if pet == "REX" and marry == "03/04/1952" and color == "YELLOW":
            return render_template("console.html")
        else:
            return render_template("security_questions.html")

@app.route("/console.html")
def console():
    return render_template("console.html")
