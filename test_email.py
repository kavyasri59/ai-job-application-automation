from app.services.email_sender import send_email

result = send_email(
    recipient_email="kavyasrisanniboina@gmail.com",
    subject="AI Job Application Automation - Test",
    body="""Hello,

This is a test email from my AI Job Application Automation project.

Regards,
Sanniboina Kavyasri
"""
)

print(result)
