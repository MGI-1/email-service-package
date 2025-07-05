def get_welcome_email_template(user_name, user_email):
    """Welcome email template for new users"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to SalesWit</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
            <h1 style="color: white; margin: 0; font-size: 28px;">Welcome to SalesWit!</h1>
            <p style="color: white; margin: 10px 0 0 0; font-size: 16px;">Your journey to smarter sales intelligence starts here</p>
        </div>
        
        <div style="background: #f8f9fa; padding: 30px; border-radius: 0 0 10px 10px;">
            <h2 style="color: #333; margin-top: 0;">Hi {user_name}! 👋</h2>
            
            <p>Thank you for joining SalesWit! We're excited to help you generate comprehensive company intelligence reports and stakeholder insights.</p>
            
            <div style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #ff7e00;">
                <h3 style="margin-top: 0; color: #ff7e00;">Get Started in 3 Easy Steps:</h3>
                <ol style="padding-left: 20px;">
                    <li><strong>Create Your First CD Report:</strong> Enter a company name and website to generate detailed insights</li>
                    <li><strong>Explore Stakeholder Intelligence:</strong> Discover key decision-makers and their potential objections</li>
                    <li><strong>Review Business Intelligence:</strong> Access comprehensive company analysis and market positioning</li>
                </ol>
            </div>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://your-app-url.com/create-cd" style="background: #ff7e00; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">Create Your First Report</a>
            </div>
            
            <div style="background: #e8f4ff; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <h4 style="margin-top: 0; color: #1e40af;">💡 Pro Tip:</h4>
                <p style="margin-bottom: 0;">For best results, provide specific stakeholder names when creating your CD reports. This helps our AI generate more targeted insights and objection handling strategies.</p>
            </div>
            
            <p>If you have any questions or need assistance, our support team is here to help at <a href="mailto:support@saleswit.com">support@saleswit.com</a>.</p>
            
            <p>Happy selling!<br>
            <strong>The SalesWit Team</strong></p>
        </div>
        
        <div style="text-align: center; padding: 20px; color: #666; font-size: 12px;">
            <p>© 2025 SalesWit. All rights reserved.<br>
            You received this email because you signed up for a SalesWit account.</p>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Welcome to SalesWit, {user_name}!
    
    Thank you for joining SalesWit! We're excited to help you generate comprehensive company intelligence reports and stakeholder insights.
    
    Get Started in 3 Easy Steps:
    1. Create Your First CD Report: Enter a company name and website to generate detailed insights
    2. Explore Stakeholder Intelligence: Discover key decision-makers and their potential objections  
    3. Review Business Intelligence: Access comprehensive company analysis and market positioning
    
    Visit: https://your-app-url.com/create-cd
    
    Pro Tip: For best results, provide specific stakeholder names when creating your CD reports.
    
    Questions? Contact us at support@saleswit.com
    
    Happy selling!
    The SalesWit Team
    """
    
    return html_content, text_content

def get_email_verification_template(user_name, verification_link):
    """Email verification template"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Verify Your Email - SalesWit</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
            <h1 style="color: white; margin: 0; font-size: 28px;">Verify Your Email</h1>
            <p style="color: white; margin: 10px 0 0 0; font-size: 16px;">One more step to get started with SalesWit</p>
        </div>
        
        <div style="background: #f8f9fa; padding: 30px; border-radius: 0 0 10px 10px;">
            <h2 style="color: #333; margin-top: 0;">Hi {user_name}! 👋</h2>
            
            <p>Thanks for signing up for SalesWit! To complete your registration and start creating CD reports, please verify your email address.</p>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="{verification_link}" style="background: #ff7e00; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">Verify Email Address</a>
            </div>
            
            <div style="background: #fef3cd; padding: 15px; border-radius: 5px; margin: 20px 0; border-left: 4px solid #fbbf24;">
                <h4 style="margin-top: 0; color: #92400e;">⏰ Important:</h4>
                <p style="margin-bottom: 0;">This verification link will expire in 24 hours. If you don't verify your email within this time, you'll need to sign up again.</p>
            </div>
            
            <p>If the button doesn't work, copy and paste this link into your browser:</p>
            <p style="word-break: break-all; background: #f1f1f1; padding: 10px; border-radius: 3px; font-family: monospace;">{verification_link}</p>
            
            <p>If you didn't create an account with SalesWit, you can safely ignore this email.</p>
            
            <p>Best regards,<br>
            <strong>The SalesWit Team</strong></p>
        </div>
        
        <div style="text-align: center; padding: 20px; color: #666; font-size: 12px;">
            <p>© 2025 SalesWit. All rights reserved.</p>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Verify Your Email - SalesWit
    
    Hi {user_name}!
    
    Thanks for signing up for SalesWit! To complete your registration and start creating CD reports, please verify your email address.
    
    Click here to verify: {verification_link}
    
    Important: This verification link will expire in 24 hours.
    
    If you didn't create an account with SalesWit, you can safely ignore this email.
    
    Best regards,
    The SalesWit Team
    """
    
    return html_content, text_content

def get_usage_warning_template(user_name, current_usage, usage_limit, plan_type, percentage_used):
    """Usage limit warning template"""
    
    # Determine warning level and colors
    if percentage_used >= 90:
        warning_color = "#ef4444"
        warning_bg = "#fee2e2"
        warning_border = "#dc2626"
        warning_title = "🚨 Action Required:"
        warning_text = "You have very few reports remaining this month. Consider upgrading to continue generating CD reports without interruption."
    else:
        warning_color = "#f59e0b"
        warning_bg = "#fef3cd"
        warning_border = "#f59e0b"
        warning_title = "⚠️ Heads Up:"
        warning_text = "You're getting close to your monthly limit. Consider upgrading to ensure uninterrupted access to CD reports."
    
    # Determine progress bar color
    if percentage_used >= 90:
        progress_color = "#ef4444"
    elif percentage_used >= 80:
        progress_color = "#f59e0b"
    else:
        progress_color = "#10b981"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Usage Alert - SalesWit</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
            <h1 style="color: white; margin: 0; font-size: 28px;">📊 Usage Alert</h1>
            <p style="color: white; margin: 10px 0 0 0; font-size: 16px;">You're approaching your monthly limit</p>
        </div>
        
        <div style="background: #f8f9fa; padding: 30px; border-radius: 0 0 10px 10px;">
            <h2 style="color: #333; margin-top: 0;">Hi {user_name}! 📈</h2>
            
            <p>You've been actively using SalesWit to generate valuable company intelligence - that's great! However, you're approaching your monthly usage limit.</p>
            
            <div style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #f59e0b;">
                <h3 style="margin-top: 0; color: #d97706;">Current Usage Summary:</h3>
                <div style="display: flex; justify-content: space-between; align-items: center; margin: 15px 0;">
                    <span><strong>Plan:</strong> {plan_type}</span>
                    <span><strong>Used:</strong> {current_usage} of {usage_limit} reports</span>
                </div>
                <div style="background: #f3f4f6; border-radius: 10px; height: 20px; margin: 15px 0;">
                    <div style="background: {progress_color}; height: 100%; width: {percentage_used:.0f}%; border-radius: 10px; transition: width 0.3s ease;"></div>
                </div>
                <p style="text-align: center; margin: 5px 0 0 0; font-weight: bold; color: {warning_color};">{percentage_used:.0f}% Used</p>
            </div>
            
            <div style="background: {warning_bg}; padding: 15px; border-radius: 5px; margin: 20px 0; border-left: 4px solid {warning_border};">
                <h4 style="margin-top: 0; color: {warning_color};">{warning_title}</h4>
                <p style="margin-bottom: 0;">{warning_text}</p>
            </div>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://your-app-url.com/pricing" style="background: #ff7e00; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; margin-right: 10px;">Upgrade Plan</a>
                <a href="https://your-app-url.com/view-cds" style="background: #6b7280; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">View My Reports</a>
            </div>
            
            <div style="background: #e8f4ff; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <h4 style="margin-top: 0; color: #1e40af;">💡 Why Upgrade?</h4>
                <ul style="margin-bottom: 0; padding-left: 20px;">
                    <li>Higher monthly report limits</li>
                    <li>Priority processing for faster results</li>
                    <li>Advanced stakeholder insights</li>
                    <li>Priority customer support</li>
                </ul>
            </div>
            
            <p>Questions about your usage or our plans? Contact us at <a href="mailto:support@saleswit.com">support@saleswit.com</a>.</p>
            
            <p>Keep selling smart!<br>
            <strong>The SalesWit Team</strong></p>
        </div>
        
        <div style="text-align: center; padding: 20px; color: #666; font-size: 12px;">
            <p>© 2025 SalesWit. All rights reserved.</p>
        </div>
    </body>
    </html>
    """
    
    # Create text content
    if percentage_used >= 90:
        text_warning = "Action Required: You have very few reports remaining this month. Consider upgrading to continue generating CD reports without interruption."
    else:
        text_warning = "Heads Up: You're getting close to your monthly limit. Consider upgrading to ensure uninterrupted access to CD reports."
    
    text_content = f"""
    Usage Alert - SalesWit
    
    Hi {user_name}!
    
    You've been actively using SalesWit to generate valuable company intelligence - that's great! However, you're approaching your monthly usage limit.
    
    Current Usage Summary:
    Plan: {plan_type}
    Used: {current_usage} of {usage_limit} reports ({percentage_used:.0f}% Used)
    
    {text_warning}
    
    Why Upgrade?
    - Higher monthly report limits
    - Priority processing for faster results  
    - Advanced stakeholder insights
    - Priority customer support
    
    Upgrade: https://your-app-url.com/pricing
    View Reports: https://your-app-url.com/view-cds
    
    Questions? Contact us at support@saleswit.com
    
    Keep selling smart!
    The SalesWit Team
    """
    
    return html_content, text_content