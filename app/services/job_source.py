def normalize_job(job):
    return {
        "title": job.get("title", "").strip(),
        "company": job.get("company", "").strip(),
        "location": job.get("location", "").strip(),
        "url": job.get("url", "").strip(),
        "description": job.get("description", "").strip(),
        "source": job.get("source", "").strip()
    }


def fetch_jobs():
    jobs = [
        {
            "title": "Junior DevOps Engineer",
            "company": "Reizend (P) Ltd",
            "location": "Trivandrum",
            "url": "https://example.com/job1",
            "description": """
Junior DevOps Engineer

Experience: Fresher / 0-2 years

Skills:
AWS
Docker
Kubernetes
CI/CD
Linux

Location: Trivandrum
""",
            "source": "demo"
        },

        {
            "title": "DevOps Engineer",
            "company": "ABC Technologies",
            "location": "Bangalore",
            "url": "https://example.com/job2",
            "description": """
DevOps Engineer

Experience: 0-2 years

Skills:
AWS
Terraform
Jenkins
Docker
Kubernetes
Python

Location: Bangalore
""",
            "source": "demo"
        },

        {
            "title": "Cloud Engineer",
            "company": "XYZ Cloud",
            "location": "Hyderabad",
            "url": "https://example.com/job3",
            "description": """
Cloud Engineer

Experience: Fresher / 1 year

Skills:
AWS
Linux
Git
Terraform
Ansible

Location: Hyderabad
""",
            "source": "demo"
        }
    ]

    return [normalize_job(job) for job in jobs]
