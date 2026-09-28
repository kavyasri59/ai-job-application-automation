import pymupdf


def extract_text_from_pdf(pdf_path: str):

    document = pymupdf.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_resume_skills(text: str):

    known_skills = [
        "AWS",
        "Azure",
        "GCP",
        "EC2",
        "S3",
        "RDS",
        "Lambda",
        "VPC",
        "Docker",
        "Kubernetes",
        "EKS",
        "Terraform",
        "Jenkins",
        "Git",
        "GitHub",
        "GitHub Actions",
        "Linux",
        "Ubuntu",
        "Python",
        "Bash",
        "Ansible",
        "Helm",
        "ArgoCD",
        "Prometheus",
        "Grafana",
        "MySQL",
        "PostgreSQL",
        "Django",
        "Flask",
        "FastAPI",
        "Nginx",
        "CI/CD"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in known_skills:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def analyze_resume(pdf_path: str):

    text = extract_text_from_pdf(pdf_path)

    skills = extract_resume_skills(text)

    return {
        "skills": skills,
        "text": text
    }
