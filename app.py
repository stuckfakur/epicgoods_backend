from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from config import Config
from models import db
from models.User import TokenBlacklist
from routes.AuthRoutes import auth_bp
from routes.CategoryRoutes import category_bp
from routes.FollowerRoutes import follower_bp
from routes.LocationRoute import location_bp
from routes.ProductRoutes import product_bp
from routes.SellerRoute import seller_bp
from routes.UserRoute import user_bp
from utils.check_db import connection_check

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
app.register_blueprint(auth_bp, url_prefix='/auth')


swagger = Swagger(app)
connection_check()

# CORS(
#     app,
#     supports_credentials=True,
#     origins=[
#         'http://localhost:3000', 'http://127.0.0.1:3000',
#     ],
#     allow_headers=['Content-Type', 'Authorization'],
#     methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
# )

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}},
     supports_credentials=True)


@app.route('/')
def index():
    return "Helo everybody, this is a Final Project"


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    token = TokenBlacklist.query.filter_by(jti=jti).first()
    return token is not None


if __name__ == "__main__":
    app.run(debug=True)
