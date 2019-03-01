'''
Created on 10 Feb 2019

@author: A.Braca
'''
from flask import Flask, request, session, redirect, url_for, render_template, flash
from models import User, display
from werkzeug.debug import DebuggedApplication



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
    age = request.form["age"]
    religion = request.form["religion"]
    

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
                        age,
                        religion,
                        recreation)

    return redirect(url_for("index"))




@app.route("/values", methods=["GET","POST"])
def values():
    return render_template("values.html")


@app.route("/add_values", methods=["POST"])
def add_values():
    
    values_list = ["v1","v2","v3","v4","v5","v6","v7","v8","v9","v10","v11","v12","v13",
                    "v14","v15","v16","v17","v18","v19","v20","v21","v22","v23","v24",
                    "v25","v26","v27","v28","v29","v30","v31","v32","v33"]
    likert = []
    for element in values_list:
        score = request.form[element]
        likert.append(score)
    user = User(session["username"])
    
    user.add_values(likert)
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



@app.route("/add_argument", methods=["POST"])
def add_argument():
    issue = request.form["issue"]
    side = request.form["side"]
    type_schema = request.form["type_schema"]
    premise_type=request.form["premise_type"]
    argu = request.form["argu"] 
    major_premise = request.form["major_premise"]
    minor_premise = request.form["minor_premise"]
    conclusion = request.form["conclusion"]
    type_dialog = request.form["type_dialog"]
    influence_social = request.form["influence_social"]
    support = request.form["support"]
    source =request.form["source"]
    
    
    user = User(session["username"])
   
    user.add_arguments(issue, 
                        side,
                        type_schema,
                        premise_type, 
                        argu, 
                        major_premise,
                        "",
                        minor_premise,
                        conclusion,
                        type_dialog,
                        influence_social,
                        support,
                        source)

    return redirect(url_for("index"))

@app.route("/room_discussions", methods=["GET","POST"])
def room_discussions():
    return render_template("dialogs_front.html") 

 
@app.route('/dialogs')
def dialogs():
    """Renders the dialogs page."""
    
    posts = display()
    #postsA = display()
    #postsB = display()
 

    return render_template('dialogs.html', posts = display())
           

@app.route("/statements", methods=["GET","POST"])
def statements():
    return render_template("argument_save.html")


@app.route("/like_argument/<argument_id>")
def like_argument(argument_id):
    username = session.get("username")
   

    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))

    user = User(username)
    
    user.like_argument(argument_id)
    flash("Liked Dialogs.")
    return redirect(request.referrer)



 
@app.route("/add_ratings", methods=["POST"])
def add_ratings():
    """Save rates table."""

    # keys = ["r5","r4","r3","r2","r1"]
    # stars = []
    # for element in keys:
    #     score = request.form[element]
    #     stars.append(score)
    # user = User(session["username"])
    # user.add_values(stars)
    # return redirect(request.referrer)
    rating = int(request.form["rating_value"])
    user = User(session["username"])
    
    user.add_ratings(rating)  # One of 1, 2, 3, 4, 5
   
    return "OK"

   



# --------Display the  dialog experimemts###
@app.route("/profile/<username>")
def profile(username):
    user1 = User(session.get("username"))
   

  

    return render_template("profile.html", username=username, posts=posts)

@app.route('/postquestions')
def postquestions():
    """Renders the post experiments page."""

    return render_template("post_questions01.html")

@app.route('/postquestions_02')
def post_questions02():
    """Renders the post experiments page."""

    return render_template("post_questions02.html")

@app.route("/logout")
def logout():
    session.pop("username")

    flash("Logged out.")
    return redirect(url_for("index"))




if __name__ == '__main__':

    app.run(debug=True)
