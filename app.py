from flask import Flask, render_template, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    imagePath = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article id: {self.title} - {self.content} - {self.imagePath}>"


@app.route("/")
def index():
    articles = Article.query.order_by(desc(Article.created_at)).all()

    if request.headers.get("Accept") == "application/json":
        articles_json = [
            {
                "id": article.id,
                "title": article.title,
                "content": article.content,
                "imagePath": article.imagePath,
                "created_at": article.created_at,
            }
            for article in articles
        ]
        return jsonify(articles_json)
    else:
        return render_template("index.html", articles=articles)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/article/<int:id>")
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


@app.route("/article/create", methods=["GET", "POST"])
def createArticle():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if "image" in request.files:
            image = request.files["image"]
            image.save(f"./static/uploaded_images/{image.filename}")

            imagePath = f"/{image.filename}"

        new_article = Article(title=title, content=content, imagePath=imagePath)

    else:
        return render_template("createArticle.html")

    try:
        db.session.add(new_article)
        db.session.commit()
        return redirect("/")
    except:
        return "Error"  # Return a render template of an error page


@app.route("/article/update/<int:id>", methods=["PUT"])
def updateArticle(id):
    article = Article.query.get_or_404(id)

    if request.method == "PUT":
        article.title = request.form["title"]
        article.content = request.form["content"]
        article.imagePath = request.form["imagePath"]
    else:
        return render_template("index.html", article=article)

    try:
        db.session.commit()
        return redirect("/")
    except:
        return "Error"  # Return a render template of an error page


@app.route("/article/delete/<int:id>", methods=["DELETE"])
def deleteArticle(id):
    article_to_delete = Article.query.get_or_404(id)

    try:
        db.session.delete(article_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "Error"  # Return a render template of an error page


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=3000)
