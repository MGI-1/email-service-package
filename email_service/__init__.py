from .mailer import init_mail, mail
from flask_mail import Message
from flask import current_app
import logging
import os

__version__ = '0.1.1'

# Global state
_email_service = None
_initialized = False

class EmailService:
    """Simple email service class"""
    
    def __init__(self, app=None, email_config=None):
        self.app = app
        
        if app is not None:
            self.init_app(app, email_config)
    
    def init_app(self, app, email_config=None):
        """Initialize email service with Flask app"""
        self.app = app
        
        # Configure email from provided config or environment
        if email_config:
            app.config.update(email_config)
        else:
            app.config.update({
                'MAIL_SERVER': os.getenv('MAIL_SERVER'),
                'MAIL_PORT': int(os.getenv('MAIL_PORT', 587)),
                'MAIL_USE_TLS': True,
                'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
                'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
                'MAIL_DEFAULT_SENDER': os.getenv('MAIL_DEFAULT_SENDER'),
            })
        
        init_mail(app)
        logging.info("Email service initialized")
    
    def send_email(self, recipient, subject, html_body, text_body=None):
        """Generic email sending function"""
        try:
            with self.app.app_context():
                msg = Message(
                    subject=subject,
                    recipients=[recipient] if isinstance(recipient, str) else recipient,
                )
                
                msg.html = html_body
                if text_body:
                    msg.body = text_body
                
                mail.send(msg)
                logging.info(f"Email sent successfully to {recipient}")
                return True
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")
            return False
    
    def send_welcome_email_saleswit(self, user_email, user_name):
        """Send welcome email for SalesWit"""
        try:
            with self.app.app_context():
                from email_templates import get_saleswit_welcome_email_template
                html_content, text_content = get_saleswit_welcome_email_template(user_name, user_email)
                return self.send_email(user_email, "Welcome to SalesWit!", html_content, text_content)
        except Exception as e:
            logging.error(f"Error sending SalesWit welcome email: {str(e)}")
            return False
    
    def send_usage_warning_email_saleswit(self, user_email, user_name, requests_used, requests_limit, plan_name):
        """Send usage warning email for SalesWit"""
        try:
            with self.app.app_context():
                from email_templates import get_saleswit_usage_warning_template
                percentage_used = (requests_used / requests_limit * 100) if requests_limit > 0 else 0
                
                html_content, text_content = get_saleswit_usage_warning_template(
                    user_name, requests_used, requests_limit, plan_name, percentage_used
                )
                return self.send_email(user_email, "Usage Warning - SalesWit", html_content, text_content)
        except Exception as e:
            logging.error(f"Error sending SalesWit usage warning email: {str(e)}")
            return False
    
    def send_welcome_email_marketfit(self, user_email, user_name):
        """Send welcome email for MarketFit"""
        try:
            with self.app.app_context():
                from email_templates import get_marketfit_welcome_email_template
                html_content, text_content = get_marketfit_welcome_email_template(user_name, user_email)
                return self.send_email(user_email, "Welcome to MarketFit!", html_content, text_content)
        except Exception as e:
            logging.error(f"Error sending MarketFit welcome email: {str(e)}")
            return False
    
    def send_usage_warning_email_marketfit(self, user_email, user_name, document_pages_used, document_pages_limit, perplexity_requests_used, perplexity_requests_limit, plan_name):
        """Send usage warning email for MarketFit"""
        try:
            with self.app.app_context():
                from email_templates import get_marketfit_usage_warning_template
                
                doc_percentage = (document_pages_used / document_pages_limit * 100) if document_pages_limit > 0 else 0
                req_percentage = (perplexity_requests_used / perplexity_requests_limit * 100) if perplexity_requests_limit > 0 else 0
                overall_percentage = max(doc_percentage, req_percentage)
                
                html_content, text_content = get_marketfit_usage_warning_template(
                    user_name, 
                    document_pages_used, document_pages_limit,
                    perplexity_requests_used, perplexity_requests_limit,
                    plan_name, overall_percentage
                )
                return self.send_email(user_email, "Usage Warning - MarketFit", html_content, text_content)
        except Exception as e:
            logging.error(f"Error sending MarketFit usage warning email: {str(e)}")
            return False

def init_email_service(app=None, email_config=None):
    """Initialize the email service with a Flask app"""
    global _email_service, _initialized
    
    service = EmailService(app, email_config)
    
    if app:
        _email_service = service
        _initialized = True
    
    return service

# Simple convenience functions
def send_welcome_email_saleswit(user_email, user_name):
    """Send welcome email for SalesWit"""
    if not _initialized or not _email_service:
        logging.error("Email service not initialized. Call init_email_service() first.")
        return False
    return _email_service.send_welcome_email_saleswit(user_email, user_name)

def send_usage_warning_email_saleswit(user_email, user_name, requests_used, requests_limit, plan_name):
    """Send usage warning email for SalesWit"""
    if not _initialized or not _email_service:
        logging.error("Email service not initialized. Call init_email_service() first.")
        return False
    return _email_service.send_usage_warning_email_saleswit(user_email, user_name, requests_used, requests_limit, plan_name)

def send_welcome_email_marketfit(user_email, user_name):
    """Send welcome email for MarketFit"""
    if not _initialized or not _email_service:
        logging.error("Email service not initialized. Call init_email_service() first.")
        return False
    return _email_service.send_welcome_email_marketfit(user_email, user_name)

def send_usage_warning_email_marketfit(user_email, user_name, document_pages_used, document_pages_limit, perplexity_requests_used, perplexity_requests_limit, plan_name):
    """Send usage warning email for MarketFit"""
    if not _initialized or not _email_service:
        logging.error("Email service not initialized. Call init_email_service() first.")
        return False
    return _email_service.send_usage_warning_email_marketfit(user_email, user_name, document_pages_used, document_pages_limit, perplexity_requests_used, perplexity_requests_limit, plan_name)