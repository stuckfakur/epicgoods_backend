import os

import dotenv
from mailjet_rest import Client
from dotenv import load_dotenv
load_dotenv()

class Config:
    HOST = os.getenv('DB_HOST')
    DATABASE = os.getenv('DB_DATABASE')
    USERNAME = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('DB_PASSWORD')

    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATION = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    # Mail Settings
    MAIL_DEFAULT_SENDER = "noreply@epicgoods.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    API_KEY = os.environ['MJ_APIKEY_PUBLIC']
    API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

    mailjet = Client(auth=(API_KEY, API_SECRET))

    # Print the database URI for debugging
print(Config.SQLALCHEMY_DATABASE_URI)