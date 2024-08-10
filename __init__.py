from flask_mail import Mail


def init_app(app):
    mail = Mail(app)