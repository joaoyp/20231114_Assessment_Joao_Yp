from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    FileField,
    TextAreaField,
)
from wtforms.validators import DataRequired


class CreateArticle(FlaskForm):
    title = StringField("Title:", validators=[DataRequired()])
    content = TextAreaField("Content:", validators=[DataRequired()])
    image = FileField(
        "Image:",
        validators=[DataRequired()],
    )
    submit = SubmitField("Create Article")


class UpdateArticle(FlaskForm):
    title = StringField("Title:", validators=[DataRequired()])
    content = TextAreaField("Content:", validators=[DataRequired()])
    image = FileField(
        "Image:",
        validators=[DataRequired()],
    )
    submit = SubmitField("Update Article")
