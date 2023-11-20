from flask import Flask, render_template
from blueprints.articles.routes import articles_bp
from blueprints.common.routes import common_bp
from blueprints.auth.routes import auth_bp
from database.db import init_db
from blueprints.auth.routes import login_manager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SECRET_KEY"] = "not_so_secret"
init_db(app)

login_manager.init_app(app)
login_manager.login_view = "auth.signIn"

app.register_blueprint(articles_bp)
app.register_blueprint(common_bp)
app.register_blueprint(auth_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=3000)
