import os

from flask import Blueprint, render_template, request, jsonify, redirect
from sqlalchemy import desc
from .models import Article
from database.db import db
from .forms import CreateArticle, UpdateArticle
from werkzeug.utils import secure_filename
import uuid

articles_bp = Blueprint("articles", __name__, template_folder="/templates")


@articles_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    articles = Article.query.order_by(desc(Article.created_at)).paginate(
        page=page, per_page=8
    )

    recentArticles = Article.query.order_by(desc(Article.created_at))[:4]

    if request.headers.get("Accept") == "application/json":
        articles_json = [
            {
                "id": article.id,
                "title": article.title,
                "content": article.content,
                "imagePath": article.imagePath,
                "created_at": article.created_at,
            }
            for article in articles.items
        ]
        return jsonify(articles_json)
    else:
        return render_template(
            "index.html", articles=articles, recentArticles=recentArticles
        )


@articles_bp.route("/article/<int:id>")
def getArticle(id):
    article = Article.query.get_or_404(id)

    if request.headers.get("Accept") == "application/json":
        article_json = {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "imagePath": article.imagePath,
            "created_at": article.created_at,
        }

        return jsonify(article_json)
    else:
        return render_template("article.html", article=article)


@articles_bp.route("/article/create", methods=["GET", "POST"])
def createArticle():
    form = CreateArticle()

    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data

            if form.image.data:
                imageName = secure_filename(str(uuid.uuid4()) + ".jpg")
                form.image.data.save(f"static/uploaded_images/{imageName}")
                imagePath = f"/{imageName}"

        new_article = Article(title=title, content=content, imagePath=imagePath)

    else:
        return render_template("createArticle.html", form=form)

    try:
        db.session.add(new_article)
        db.session.commit()
        return redirect("/")
    except:
        return render_template(
            "error.html",
            message="An error occurred while creating the article. Please try again.",
        )


@articles_bp.route("/article/update/<int:id>", methods=["GET", "POST"])
def updateArticle(id):
    article = Article.query.get_or_404(id)
    form = UpdateArticle(obj=article)

    if request.method == "POST":
        if form.validate_on_submit():
            article.title = form.title.data
            article.content = form.content.data

            if form.image.data:
                imageName = secure_filename(str(uuid.uuid4()) + ".jpg")
                form.image.data.save(f"static/uploaded_images/{imageName}")
                article.imagePath = f"/{imageName}"
    else:
        return render_template("updateArticle.html", article=article, form=form)

    try:
        db.session.commit()
        return redirect("/")
    except:
        return render_template(
            "error.html",
            message="An error occurred while updating the article. Please try again.",
        )


@articles_bp.route("/article/delete/<int:id>", methods=["POST"])
def deleteArticle(id):
    article_to_delete = Article.query.get_or_404(id)

    try:
        if article_to_delete.imagePath:
            if os.path.exists("static/uploaded_images" + article_to_delete.imagePath):
                os.remove("static/uploaded_images" + article_to_delete.imagePath)
        db.session.delete(article_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return render_template(
            "error.html",
            message="An error occurred while deleting the article. Please try again.",
        )
