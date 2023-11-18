from flask import Blueprint, render_template, request, redirect
from .forms import ContactForm

common_bp = Blueprint("common_routes", __name__, template_folder="/templates")


@common_bp.route("/about")
def about():
    return render_template("about.html")


@common_bp.route("/contacts", methods=["GET", "POST"])
def createArticle():
    form = ContactForm()

    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message = form.message.data

            return redirect("/")
    else:
        return render_template("contacts.html", form=form)
