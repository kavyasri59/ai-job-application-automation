import re


KNOWN_SKILLS = [
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Jenkins",
    "Git",
    "GitHub",
    "GitHub Actions",
    "Linux",
    "Python",
    "Bash",
    "Ansible",
    "Helm",
    "ArgoCD",
    "Prometheus",
    "Grafana",
    "CI/CD",
    "Azure",
    "GCP",
    "MySQL",
    "PostgreSQL",
    "Django",
    "Flask",
    "FastAPI"
]


def extract_skills(text: str):
    found_skills = []

    text_lower = text.lower()

    for skill in KNOWN_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def extract_experience(text: str):
    patterns = [
        r"\d+\s*[-–]\s*\d+\s*years?",
        r"\d+\+?\s*years?",
        r"\d+\s*to\s*\d+\s*years?"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(0)

    return "Not specified"


def extract_location(text: str):

    patterns = [
        r"(?:location|work location|based in)\s*[:\-]?\s*([A-Za-z ,]+)",
        r"\bin\s+(Bangalore|Bengaluru|Hyderabad|Chennai|Pune|Mumbai|Delhi|Gurgaon|Gurugram|Noida|Ahmedabad|Kolkata)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

    return "Not specified"


def extract_job_title(text: str):
    job_titles = [
        "Junior DevOps Engineer",
        "Senior DevOps Engineer",
        "DevOps Engineer",
        "Cloud Engineer",
        "Site Reliability Engineer",
        "SRE",
        "DevOps Intern",
        "Cloud Intern",
        "Software Engineer",
        "Backend Developer",
        "Python Developer",
        "AWS Engineer"
    ]

    text_lower = text.lower()

    for title in job_titles:
        if title.lower() in text_lower:
            return title

    return "Not specified"


def analyze_job_description(text: str):
    return {
        "job_title": extract_job_title(text),
        "experience": extract_experience(text),
        "location": extract_location(text),
        "skills": extract_skills(text)
    }
