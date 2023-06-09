from flask import Flask, render_template
from app.modules.shop.products import bp
from app.modules.auth import users
from app.modules.admin import admin


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(admin.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
    return app
