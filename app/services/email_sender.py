import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(
    recipient_email,
    subject,
    body,
    attachment_path=None
):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    sender_email = os.getenv("SENDER_EMAIL")

    if not smtp_username:
        raise ValueError("SMTP_USERNAME is not configured")

    if not smtp_password:
        raise ValueError("SMTP_PASSWORD is not configured")

    if not sender_email:
        raise ValueError("SENDER_EMAIL is not configured")

    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.set_content(body)

    if attachment_path:
        with open(attachment_path, "rb") as file:
            file_data = file.read()

        filename = os.path.basename(attachment_path)

        message.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename=filename
        )

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

    return {
        "status": "success",
        "message": "Email sent successfully"
    }
