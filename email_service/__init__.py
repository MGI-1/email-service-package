from .mailer import init_mail, mail
from flask_mail import Message
import logging

__version__ = '0.1.0'

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