from flask_mail import Mail, Message
import logging

# Initialize mail instance
mail = Mail()

def init_mail(app):
    """Initialize mail with the given Flask app"""
    # Initialize mail with the app
    mail.init_app(app)
    logging.info("Email service initialized")


   