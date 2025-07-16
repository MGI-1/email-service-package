from .mailer import init_mail, mail
from flask_mail import Message
from flask import current_app
import logging

__version__ = '0.1.1'

def send_email(recipient, subject, html_body, text_body=None):
    """
    Generic email sending function
    
    Parameters:
    - recipient (str): The recipient's email address
    - subject (str): Email subject
    - html_body (str): HTML content of the email
    - text_body (str, optional): Plain text content of the email
    """
    try:
        # Create message
        msg = Message(
            subject=subject,
            recipients=[recipient] if isinstance(recipient, str) else recipient,
        )
        
        # Set email content
        msg.html = html_body
        if text_body:
            msg.body = text_body
        
        # Send email
        mail.send(msg)
        logging.info(f"Email sent successfully to {recipient}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {recipient}: {str(e)}")
        return False

# SalesWit Email Functions
def send_welcome_email_saleswit(user_email, user_name):
    """Send welcome email for SalesWit"""
    try:
        # Import template from app's email_templates module
        from email_templates import get_saleswit_welcome_email_template
        
        html_content, text_content = get_saleswit_welcome_email_template(user_name, user_email)
        return send_email(user_email, "Welcome to SalesWit!", html_content, text_content)
        
    except ImportError as e:
        logging.error(f"Could not import SalesWit welcome email template: {str(e)}")
        logging.error("Make sure 'email_templates.py' exists in your app with 'get_saleswit_welcome_email_template' function")
        return False
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending SalesWit welcome email: {str(e)}")
        else:
            print(f"Error sending SalesWit welcome email: {str(e)}")
        return False

def send_usage_warning_email_saleswit(user_email, user_name, requests_used, requests_limit, plan_name):
    """
    Send usage warning email for SalesWit
    
    Parameters:
    - user_email (str): User's email address
    - user_name (str): User's display name
    - requests_used (int): Number of requests used
    - requests_limit (int): Total request limit for the plan
    - plan_name (str): Name of the subscription plan
    """
    try:
        # Import template from app's email_templates module
        from email_templates import get_saleswit_usage_warning_template
        
        percentage_used = (requests_used / requests_limit * 100) if requests_limit > 0 else 0
        
        html_content, text_content = get_saleswit_usage_warning_template(
            user_name, requests_used, requests_limit, plan_name, percentage_used
        )
        return send_email(user_email, "Usage Warning - SalesWit", html_content, text_content)
        
    except ImportError as e:
        logging.error(f"Could not import SalesWit usage warning email template: {str(e)}")
        logging.error("Make sure 'email_templates.py' exists in your app with 'get_saleswit_usage_warning_template' function")
        return False
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending SalesWit usage warning email: {str(e)}")
        else:
            print(f"Error sending SalesWit usage warning email: {str(e)}")
        return False

# MarketFit Email Functions
def send_welcome_email_marketfit(user_email, user_name):
    """Send welcome email for MarketFit"""
    try:
        # Import template from app's email_templates module
        from email_templates import get_marketfit_welcome_email_template
        
        html_content, text_content = get_marketfit_welcome_email_template(user_name, user_email)
        return send_email(user_email, "Welcome to MarketFit!", html_content, text_content)
        
    except ImportError as e:
        logging.error(f"Could not import MarketFit welcome email template: {str(e)}")
        logging.error("Make sure 'email_templates.py' exists in your app with 'get_marketfit_welcome_email_template' function")
        return False
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending MarketFit welcome email: {str(e)}")
        else:
            print(f"Error sending MarketFit welcome email: {str(e)}")
        return False

def send_usage_warning_email_marketfit(user_email, user_name, document_pages_used, document_pages_limit, perplexity_requests_used, perplexity_requests_limit, plan_name):
    """
    Send usage warning email for MarketFit
    
    Parameters:
    - user_email (str): User's email address
    - user_name (str): User's display name
    - document_pages_used (int): Number of document pages used
    - document_pages_limit (int): Total document pages limit for the plan
    - perplexity_requests_used (int): Number of perplexity requests used
    - perplexity_requests_limit (int): Total perplexity requests limit for the plan
    - plan_name (str): Name of the subscription plan
    """
    try:
        # Import template from app's email_templates module
        from email_templates import get_marketfit_usage_warning_template
        
        # Calculate percentages
        doc_percentage = (document_pages_used / document_pages_limit * 100) if document_pages_limit > 0 else 0
        req_percentage = (perplexity_requests_used / perplexity_requests_limit * 100) if perplexity_requests_limit > 0 else 0
        overall_percentage = max(doc_percentage, req_percentage)
        
        html_content, text_content = get_marketfit_usage_warning_template(
            user_name, 
            document_pages_used, document_pages_limit,
            perplexity_requests_used, perplexity_requests_limit,
            plan_name, overall_percentage
        )
        return send_email(user_email, "Usage Warning - MarketFit", html_content, text_content)
        
    except ImportError as e:
        logging.error(f"Could not import MarketFit usage warning email template: {str(e)}")
        logging.error("Make sure 'email_templates.py' exists in your app with 'get_marketfit_usage_warning_template' function")
        return False
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending MarketFit usage warning email: {str(e)}")
        else:
            print(f"Error sending MarketFit usage warning email: {str(e)}")
        return False