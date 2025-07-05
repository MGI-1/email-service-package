from flask import current_app
try:
    from email_service import send_email
    EMAIL_SERVICE_AVAILABLE = True
except ImportError:
    EMAIL_SERVICE_AVAILABLE = False
    current_app.logger.warning("Email service not available") if current_app else print("Email service not available")

def send_welcome_email(user_email, user_name):
    if not EMAIL_SERVICE_AVAILABLE:
        print(f"Would send welcome email to {user_email}")
        return True
    
    try:
        from app.email_templates import get_welcome_email_template
        html_content, text_content = get_welcome_email_template(user_name, user_email)
        return send_email(user_email, "Welcome to SalesWit!", html_content, text_content)
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending welcome email: {str(e)}")
        else:
            print(f"Error sending welcome email: {str(e)}")
        return False

def send_verification_email(user_email, user_name, verification_token):
    if not EMAIL_SERVICE_AVAILABLE:
        print(f"Would send verification email to {user_email}")
        return True
    
    try:
        from app.email_templates import get_email_verification_template
        verification_link = f"http://localhost:5000/api/auth/verify-email/{verification_token}"
        html_content, text_content = get_email_verification_template(user_name, verification_link)
        return send_email(user_email, "Verify Your Email", html_content, text_content)
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending verification email: {str(e)}")
        else:
            print(f"Error sending verification email: {str(e)}")
        return False

def send_usage_warning_email(user_email, user_name, current_usage, usage_limit, plan_type):
    if not EMAIL_SERVICE_AVAILABLE:
        print(f"Would send usage warning email to {user_email}")
        return True
    
    try:
        from app.email_templates import get_usage_warning_template
        percentage_used = (current_usage / usage_limit) * 100
        html_content, text_content = get_usage_warning_template(
            user_name, current_usage, usage_limit, plan_type, percentage_used
        )
        return send_email(user_email, "Usage Warning", html_content, text_content)
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Error sending usage warning email: {str(e)}")
        else:
            print(f"Error sending usage warning email: {str(e)}")
        return False