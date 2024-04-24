import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_notification(sender_email, recipient_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    """Send email notification."""
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email notification sent successfully!")

    except Exception as e:
        print("An error occurred while sending email notification:", e)

# Example usage:
# send_email_notification(sender_email, recipient_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password)

# send_email_notification("01projectautomation@gmail.com", "prasannack1001@gmail.com", "hi", "test message", "smtp.gmail.com", 587, "01projectautomation@gmail.com", "GoCodePlz")