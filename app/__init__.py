from flask import Flask, render_template
from app.modules.shop.products import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
    return app
