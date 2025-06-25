from flask_mail import Mail, Message
import logging

# Initialize mail instance
mail = Mail()

def init_mail(app):
    """Initialize mail with the given Flask app"""
    # Initialize mail with the app
    mail.init_app(app)
    logging.info("Email service initialized")

def send_subscription_confirmation(recipient_email, subscription_type, payment_method, subscription_details):
    """
    Send subscription confirmation email
    
    Parameters:
    - recipient_email (str): The recipient's email address
    - subscription_type (str): Type of subscription purchased
    - payment_method (str): 'razorpay' or 'paypal'
    - subscription_details (dict): Dictionary containing subscription details
      - plan: The subscription plan name
      - amount: The amount paid
      - period: The subscription period
      - start_date: When the subscription starts
      - end_date: When the subscription ends
    """
    try:
        subject = f"Your {subscription_type} Subscription Confirmation"
        
        # Create message
        msg = Message(
            subject=subject,
            recipients=[recipient_email],
        )
        
        # Set email content
        msg.html = f"""
        <h2>Thank you for your subscription!</h2>
        <p>We're excited to confirm your {subscription_type} subscription.</p>
        <p><strong>Payment Method:</strong> {payment_method}</p>
        <p><strong>Subscription Details:</strong></p>
        <ul>
            <li><strong>Plan:</strong> {subscription_details.get('plan', 'N/A')}</li>
            <li><strong>Amount:</strong> {subscription_details.get('amount', 'N/A')}</li>
            <li><strong>Period:</strong> {subscription_details.get('period', 'N/A')}</li>
            <li><strong>Start Date:</strong> {subscription_details.get('start_date', 'N/A')}</li>
            <li><strong>End Date:</strong> {subscription_details.get('end_date', 'N/A')}</li>
        </ul>
        <p>If you have any questions, please contact our support team.</p>
        """
        
        # Send email
        mail.send(msg)
        logging.info(f"Subscription confirmation email sent to {recipient_email}")
        return True
    except Exception as e:
        logging.error(f"Failed to send subscription confirmation email: {str(e)}")
        return False

def send_payment_receipt(recipient_email, payment_details):
    """
    Send payment receipt email
    
    Parameters:
    - recipient_email (str): The recipient's email address
    - payment_details (dict): Dictionary containing payment details
      - invoice_number: The invoice or transaction ID
      - amount: The amount paid
      - date: The payment date
      - method: The payment method used
    """
    try:
        subject = f"Payment Receipt #{payment_details.get('invoice_number', '')}"
        
        # Create message
        msg = Message(
            subject=subject,
            recipients=[recipient_email],
        )
        
        # Set email content
        msg.html = f"""
        <h2>Payment Receipt</h2>
        <p>Thank you for your payment.</p>
        <p><strong>Payment Details:</strong></p>
        <ul>
            <li><strong>Invoice/Transaction:</strong> {payment_details.get('invoice_number', 'N/A')}</li>
            <li><strong>Amount:</strong> {payment_details.get('amount', 'N/A')}</li>
            <li><strong>Date:</strong> {payment_details.get('date', 'N/A')}</li>
            <li><strong>Method:</strong> {payment_details.get('method', 'N/A')}</li>
        </ul>
        <p>If you have any questions about this payment, please contact our support team.</p>
        """
        
        # Send email
        mail.send(msg)
        logging.info(f"Payment receipt email sent to {recipient_email}")
        return True
    except Exception as e:
        logging.error(f"Failed to send payment receipt email: {str(e)}")
        return False