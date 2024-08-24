from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from pydantic import BaseModel

from config import Config
from models import db
from models.User import TokenBlacklist
from routes.AuthRoutes import auth_bp
from routes.CategoryRoutes import category_bp
from routes.FollowerRoutes import follower_bp
from routes.LocationRoutes import location_bp
from routes.ProductCartRoutes import product_cart_bp
from routes.ProductRoutes import product_bp
from routes.SellerRoutes import seller_bp
from routes.TransactionRoutes import transaction_bp
from routes.UserRoutes import user_bp
from routes.VoucherRoutes import voucher_bp
from utils.check_db import connection_check

info = Info(title="test API", version="1.0.0")
jwt = {
    "type": "http",
    "scheme": "bearer",
    "bearerFormat": "JWT"
}
securityschemes = {"jwt": jwt}
app = OpenAPI(__name__, info=info, security_schemes=securityschemes)

test_tag = Tag(name="test", description="Some Test")


class BookQuery(BaseModel):
    age: int
    author: str


# app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

# app.register_blueprint(user_bp, url_prefix='/api')
# app.register_blueprint(seller_bp, url_prefix='/api')
# app.register_blueprint(location_bp, url_prefix='/api')
# app.register_blueprint(category_bp, url_prefix='/api')
# app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(follower_bp, url_prefix='/api')
# app.register_blueprint(transaction_bp, url_prefix='/api')
# app.register_blueprint(product_cart_bp, url_prefix='/api')
# app.register_blueprint(voucher_bp, url_prefix='/api')
# app.register_blueprint(auth_bp, url_prefix='/auth')

app.register_api(user_bp)
app.register_api(seller_bp)
app.register_api(location_bp)
app.register_api(product_bp)
# app.register_api(follower_bp)
app.register_api(transaction_bp)
app.register_api(product_cart_bp)
app.register_api(voucher_bp)
app.register_api(auth_bp)
app.register_api(category_bp)

swagger = Swagger(app)
connection_check()
production = "https://epicgoods-frontend-kappa.vercel.app/"

CORS(
    app,
    supports_credentials=True,
    origins=[

        'http://localhost:3000', 'http://127.0.0.1:3000', production
    ],
    allow_headers=['Content-Type', 'Authorization'],
    methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
)

#
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000", "*", production]}},
#      supports_credentials=True)


@app.get("/", summary="test", tags=[test_tag])
def index(query: BookQuery):
    return {
        "code": 0,
        "message": "ok",
        "data": [
            {"bid": 1, "age": query.age, "author": query.author},
            {"bid": 2, "age": query.age, "author": query.author}
        ]
    }


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    token = TokenBlacklist.query.filter_by(jti=jti).first()
    return token is not None


if __name__ == "__main__":
    app.run(debug=True)
