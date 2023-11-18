from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators, EmailField


class ContactForm(FlaskForm):
    name = StringField("Name:", validators=[validators.DataRequired()])
    email = EmailField("Email:", validators=[validators.DataRequired()])
    subject = StringField("Subject:", validators=[validators.DataRequired()])
    message = TextAreaField("Message:", validators=[validators.DataRequired()])
    submit = SubmitField("Send")
