'''
Created on 10 Feb 2019

@author: A.Braca
'''
from flask import Flask, request, session, redirect, url_for, render_template, flash
from models import User


from flask_debugtoolbar import DebugToolbarExtension

import sys

import pdb

import os 


app = Flask(__name__)
app.secret_key = os.urandom(24)



@app.route("/")
def index():

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User(username)

        if not user.register(password):
            flash("Alredy alredy exists")
        else:
            flash("Success")
            return redirect(url_for("login"))
        





    return render_template('register.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
       
        password = request.form["password"]

        user = User(username)

        if not user.verify_password(password):
            flash("Invalid login.")
        else:
            flash("Successfully logged in.")
            session["username"] = user.username
            flash (session["username"])
            return redirect(url_for("survey"))

    return render_template("login.html")


@app.route("/survey", methods=["GET","POST"])
def survey():
    return render_template("survey.html")

@app.route("/add_survey", methods=["POST"])
def add_survey():
    gender = request.form["gender"]
    sexuality = request.form["sexuality"]
    ethnicity = request.form["ethnicity"]
    occupation = request.form["occupation"]
    marital_status = request.form["marital_status"]
    education = request.form["education"]
    vehicle = request.form["vehicle"]
    recreation = request.form["recreation"]

    user = User(session["username"])

    if not sexuality or not vehicle or not education:
        flash("You must answer all the questions.")
    else:
        user.add_survey(gender,
                        sexuality,
                        ethnicity,
                        occupation,
                        marital_status,
                        education,
                        vehicle,
                        recreation)

    return redirect(url_for("index"))

@app.route("/personality", methods=["GET","POST"])
def personality():
    return render_template("personality.html")


@app.route("/add_personality", methods=["POST"])
def add_personality():
    personality_list = ["p1", "p2", "p5", "p8", "p10", "p12", "p18",
                        "p19", "p20", "p24", "p27", "p28", "p29", "p30",
                        "p31", "p32", "p33", "p34", "p36", "p37", "p39",
                        "p40", "p42", "p44", "p46", "p47", "p48", "p49",
                        "p50", "p51"] 
    likert = []
    for element in personality_list:
        score = request.form[element]
        likert.append(score)
    user = User(session["username"])
    user.add_personality(likert)
    return redirect(url_for("index"))


@app.route("/room_discussions", methods=["GET","POST"])
def room_discussions():
    return render_template("dialogs_front.html") 

 
@app.route('/dialogs', methods=['GET'])
def dialogs():
    """Renders the dialogs page."""
    return render_template('dialogs.html')
           

@app.route("/statements", methods=["GET","POST"])
def statements():
    return render_template("argument_save.html")

@app.route("/add_argument", methods=["POST"])
def add_argument():
    issue = request.form["issue"]
    claim_title = request.form["claim_title"]
    argument = request.form["argument"] 
    support = request.form["support"]
    refutation = request.form["refutation"]
    evidence = request.form["evidence"]
    reasons = request.form["reasons"]
    emotional_appeals = request.form["emotional_appeals"]
    linguistic_technique = request.form["linguistic_technique"]
    strength = request.form["strength"]
    
    user = User("username")
   
    user.add(issue, 
                claim_title,
                argument,
                support, 
                refutation,
                evidence,
                reasons, 
                emotional_appeals,
                linguistic_technique, 
                strength)
    return redirect(url_for("index"))

  


@app.route("/like_argument/<post_id>")
def like_argument(post_id):
    username = session.get("username")

    if not username:
        flash("You must be logged in to like a post.")
        return redirect(url_for("login"))

    user = User(username)
    user.like_argument(post_id)
    flash("Liked post.")
    return redirect(request.referrer)



# --------Display the  dialog experimemts###
@app.route("/profile/<username>")
def profile(username):
    user1 = User(session.get("username"))
    user2 = User(username)
    posts = user2.recent_posts(5)

  

    return render_template("profile.html", username=username, posts=posts)



@app.route("/logout")
def logout():

    flash("Logged out.")
    return redirect(url_for("index"))




if __name__ == '__main__':

    app.run(debug=True)