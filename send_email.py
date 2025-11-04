# send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_newsletter(recipient_email, subject, html_content):
    """
    Sends the newsletter email using Gmail's SMTP server.
    """
    sender_email = EMAIL_ADDRESS
    password = EMAIL_PASSWORD

    # Build the email
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    # Attach the HTML body
    part = MIMEText(html_content, "html")
    message.attach(part)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)
            print(f" Newsletter sent successfully to {recipient_email}")
    except Exception as e:
        print(f" Error sending email: {e}")


# Manual test
if __name__ == "__main__":
    html_body = """
    <h2> Exercise & Fitness Newsletter</h2>
    <p>Here are today's top fitness articles:</p>
    <ul>
        <li><a href="https://www.example.com">The Science of Muscle Recovery</a></li>
        <li><a href="https://www.example.com">Top 5 Mobility Exercises for Beginners</a></li>
    </ul>
    <p><i>This is a test email from your AI-Powered Newsletter Generator.</i></p>
    """
    send_newsletter("your-email@example.com", "AI-Powered Fitness Newsletter (Test)", html_body)
