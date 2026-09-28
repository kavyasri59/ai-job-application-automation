def generate_hr_message(
    candidate_name,
    job_title,
    company_name,
    matched_skills,
    hr_name="Hiring Manager"
):
    """
    Generate a professional HR application message.
    """

    skills = ", ".join(matched_skills)

    subject = f"Application for {job_title} - {candidate_name}"

    message = f"""Dear {hr_name},

I am writing to express my interest in the {job_title} position at
{company_name}.

I have hands-on experience with {skills}, along with practical
experience in AWS, Linux, Docker, CI/CD and infrastructure
automation.

I have attached my resume for your consideration. I would be
grateful for the opportunity to discuss how my skills and projects
could contribute to your team.

Thank you for your time and consideration.

Best Regards,
{candidate_name}
"""

    return {
        "subject": subject,
        "message": message
    }
