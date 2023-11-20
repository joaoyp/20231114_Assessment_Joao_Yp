from flask import Blueprint, render_template, request, redirect, flash
from database.db import db
from .models import User
from .forms import SignUp, SignIn
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
)

auth_bp = Blueprint("auth", __name__, template_folder="/templates")

bcrypt = Bcrypt()

login_manager = LoginManager()


def init_app(app):
    bcrypt.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route("/signin", methods=["GET", "POST"])
def signIn():
    form = SignIn()
    if form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect("/")
    return render_template("signin.html", form=form)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signUp():
    form = SignUp()
    if request.method == "POST":
        if form.validate_on_submit:
            password = form.password.data
            confirm_password = form.confirmPassword.data
            if confirm_password == password:
                hashed_password = bcrypt.generate_password_hash(form.password.data)
                new_user = User(username=form.username.data, password=hashed_password)
            else:
                return redirect("/signup")
    else:
        return render_template("signup.html", form=form)

    try:
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect("/")
    except:
        return render_template(
            "error.html",
            message="An error occurred while signing up. Please try again.",
        )


@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect("/")
