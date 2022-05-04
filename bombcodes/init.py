from flask import Flask, render_template

def create_app():
    '''Return the app after initializing components'''
    app = Flask(__name__)
    app.config.from_object('config')

    with app.app_context():
        @app.route('/')
        def index():
            return 'Hello world!'

    return app