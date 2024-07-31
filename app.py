from flask import Flask
from utils.check_db import connection_check

from routes.UserRoute import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/api')

connection_check()
@app.route('/')
def index():
    return "Helo everybody, this is a Final Project"


if __name__ == "__main__":
    app.run(debug=True)