from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    FileField,
    TextAreaField,
    validators,
)


class CreateArticle(FlaskForm):
    title = StringField("Title:", validators=[validators.DataRequired()])
    content = TextAreaField("Content:", validators=[validators.DataRequired()])
    image = FileField(
        "Image:",
        validators=[validators.DataRequired()],
    )
    submit = SubmitField("Create Article")


class UpdateArticle(FlaskForm):
    title = StringField("Title:", validators=[validators.DataRequired()])
    content = TextAreaField("Content:", validators=[validators.DataRequired()])
    image = FileField(
        "Image:",
        validators=[validators.DataRequired()],
    )
    submit = SubmitField("Update Article")
