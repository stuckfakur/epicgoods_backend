from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from models import db
from flask import Flask
from utils.check_db import connection_check
from flask_jwt_extended import JWTManager

from routes.UserRoute import user_bp
from routes.SellerRoute import seller_bp
from routes.LocationRoute import location_bp
from routes.CategoryRoutes import category_bp
from routes.ProductRoutes import product_bp
from routes.FollowerRoutes import follower_bp
from routes.AuthRoutes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(seller_bp, url_prefix='/api')
app.register_blueprint(location_bp, url_prefix='/api')
app.register_blueprint(category_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(follower_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')

connection_check()

CORS(
    app,
    supports_credentials=True,
    origins=[
        'http://0.0.0.0/0',
    ],
    allow_headers=['Content-Type', 'Authorization'],
    methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
)

@app.route('/')
def index():
    return "Helo everybody, this is a Final Project"


if __name__ == "__main__":
    app.run(debug=True)
