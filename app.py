from flask import Flask

from routes.UserRoute import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/api')


@app.route('/')
def index():
    return "Helo everybody, this is a Final Project"


if __name__ == "__main__":
    app.run(debug=True)
