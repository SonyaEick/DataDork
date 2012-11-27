from flask import (
    Flask, render_template, redirect, request, session, flash,
    g, get_flashed_messages, url_for, request, signals_available)
import model

app = Flask(__name__)

SECRET_KEY = 'pineapples'
app.config.from_object(__name__)

@app.route("/")
def index():
    return redirect("/login")

# @login_manager.user_loader
# def load_user(userid):
#     return User.get(userid)

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('user_id')
    return redirect("/login")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    # try:
    email_entered = str(request.form['email_field'])
    password_entered = str(request.form['password_field'])

    logged_in_user = model.session.query(model.User).filter(
        model.User.email == email_entered, 
        model.User.password == password_entered).one()

    if logged_in_user:

        session['user_id'] = logged_in_user.id
        return redirect("/profile")
    # except:
    #     flash("Invalid user id")
    #     return redirect("/login")


@app.route("/save_user", methods=["POST"])    
def new_user():
    user_email= request.form['user_email']
    user_pass= request.form['password_field']
    user_age= request.form['age_field']
    model.new_user(user_email, user_pass, user_age)
    return redirect("/profile")

    # We are making a rating. The data 
    # will be stored directly into the database
    # where the session id matches the user logged in
@app.route("/save_rating", methods=["POST"])
def new_rating():

    # current_session = session(id).one()
    # print current_session
    user_id = session['user_id']
    recipient_id = request.form.get('recipient_id')
    star1 = request.form.get('star1')
    text1 = request.form.get('text1')
    star2 = request.form.get('star2')
    text2 = request.form.get('text2')
    star3 = request.form.get('star3')
    text3 = request.form.get('text3')
    model.new_rating(user_id, recipient_id, star1, text1, star2, text2, star3, text3)
    return redirect("/profile")

@app.route("/new_feedback", methods=["POST"])
def new_feedback():
    user_id = session['user_id']
    rater_id = request.form.get('rater_id')
    print rater_id
    star1 = request.form.get('star1')
    text1 = request.form.get('text1')
    star2 = request.form.get('star2')
    text2 = request.form.get('text2')
    star3 = request.form.get('star3')
    text3 = request.form.get('text3')
    model.feedback(user_id, rater_id, star1, text1, star2, text2, star3, text3)
    return redirect("/profile")

@app.route("/profile")
def show_profile():
    # user_id = session.get("user_id", None)
    return render_template("profile.html")

@app.route("/rating")
def rating():
    all_users = model.session.query(model.User).all()
    return render_template("rating.html", users = all_users)

@app.route("/feedback")
def feedback():
    all_users = model.session.query(model.User).all()
    return render_template("feedback.html", users = all_users)

if __name__ == "__main__":
    app.run(debug = True)