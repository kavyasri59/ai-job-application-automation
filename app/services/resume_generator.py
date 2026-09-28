from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
import os


def generate_custom_resume(
    output_path,
    name,
    email,
    phone,
    github,
    linkedin,
    job_title,
    matched_skills,
    resume_text
):
    """
    Generate a job-specific resume PDF.

    Only uses information supplied by the user.
    """

    # Create output directory
    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    # Create PDF
    document = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        "NameStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=18,
        spaceAfter=6
    )

    contact_style = ParagraphStyle(
        "ContactStyle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=9,
        spaceAfter=12
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=12,
        spaceBefore=10,
        spaceAfter=5
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["Normal"],
        fontSize=9,
        leading=13
    )

    story = []

    # Name
    story.append(
        Paragraph(name, name_style)
    )

    # Contact details
    contact = (
        f"{email} | {phone}<br/>"
        f"GitHub: {github}<br/>"
        f"LinkedIn: {linkedin}"
    )

    story.append(
        Paragraph(contact, contact_style)
    )

    # Target position
    story.append(
        Paragraph(
            f"<b>Target Role:</b> {job_title}",
            body_style
        )
    )

    story.append(Spacer(1, 10))

    # Professional Summary
    story.append(
        Paragraph(
            "PROFESSIONAL SUMMARY",
            heading_style
        )
    )

    skills = ", ".join(matched_skills)

    summary = (
        f"DevOps Engineer with hands-on experience in "
        f"{skills}. Experienced in cloud infrastructure, "
        f"containerization, automation, CI/CD and Linux."
    )

    story.append(
        Paragraph(summary, body_style)
    )

    # Job matched skills
    story.append(
        Paragraph(
            "JOB-MATCHED SKILLS",
            heading_style
        )
    )

    story.append(
        Paragraph(
            skills,
            body_style
        )
    )

    # Existing resume information
    story.append(
        Paragraph(
            "RESUME INFORMATION",
            heading_style
        )
    )

    # Convert new lines into HTML breaks
    resume_text = resume_text.replace(
        "\n",
        "<br/>"
    )

    story.append(
        Paragraph(
            resume_text,
            body_style
        )
    )

    # Generate PDF
    document.build(story)

    return output_path
