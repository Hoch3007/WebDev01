from flask import Flask, render_template, url_for, request, redirect, flash, make_response
from random import randint
from flask_sqlalchemy import SQLAlchemy

# App und Einstellungen

app = Flask(__name__)

app.secret_key = '6ca97bc342cdbecabbadb5c47b006ef4'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

# Datenbank
db = SQLAlchemy(app)

# Klassen für die Datenbank

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    secret_number = db.Column(db.Integer)

    # definiert was erscheint bei print bzw. wenn das Objekt angezeigt werden soll
    def __repr__(self):
        return f"User('{self.user_name}', '{self.secret_number}')"

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/new_game", methods=["POST", "GET"])
def new_game():
    number_guess = request.form.get("guess")
    user_name = request.form.get("user_name")

    if request.method == "POST":

        user = User.query.filter_by(user_name=user_name).first()

        if user is None:
            new_user = User(user_name=user_name, secret_number=randint(0,30))
            db.session.add(new_user)
            db.session.commit()
            print(new_user)

        user = User.query.filter_by(user_name=user_name).first()
        secret = user.secret_number

        if int(number_guess) == secret:
            flash("Great. That's correct. The number was " + str(secret) +
                  ". If would like to guess another number just guess again.", "success")
            user.secret_number=randint(0,30)
            db.session.commit()

        elif int(number_guess)>secret:
            flash("Sorry, that's too high.", "danger")
        else:
            flash("Sorry, that's too low.", "danger")

        return redirect("/new_game")

    return render_template('new_game.html')


if __name__ == '__main__':
    app.run(debug=True)