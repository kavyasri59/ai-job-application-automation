# AI Job Application Automation System

An AI-powered job application automation system built with **Python, FastAPI, PostgreSQL/SQLite, Docker, and email automation**.

The goal of this project is to reduce the manual effort involved in applying for jobs by processing job descriptions, extracting important information, matching job requirements with a candidate's resume, generating personalized application emails, and sending applications through an email service.

---

# Project Overview

Applying for multiple jobs manually can be time-consuming.

This project is designed to automate the job application workflow:

```text
Job Description
       ↓
Job Data Processing
       ↓
Extract Job Role / Skills / HR Email
       ↓
Resume Processing
       ↓
Resume ↔ Job Matching
       ↓
Match Score
       ↓
Personalized Email Generation
       ↓
Email Service
       ↓
Resume Attachment
       ↓
Application Tracking
```

The project is being developed as a practical **AI + Python + DevOps** project.

---

## 🎯 Project Objectives

* Process job descriptions
* Extract job-related information
* Extract required technical skills
* Parse a candidate's resume
* Compare resume skills with job requirements
* Calculate a job/resume match score
* Generate personalized application emails
* Send application emails with resume attachments
* Store application information
* Containerize the application using Docker
* Run application services using Docker Compose
* Deploy the application on AWS EC2
* Build a foundation for CI/CD automation

---

## 🛠️ Technologies Used

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| Python           | Application development     |
| FastAPI          | REST API                    |
| Pydantic         | Data validation             |
| PyMuPDF          | Resume PDF processing       |
| SQLAlchemy       | Database interaction        |
| PostgreSQL       | Application database        |
| SQLite           | Local application tracking  |
| Docker           | Containerization            |
| Docker Compose   | Multi-container environment |
| Uvicorn          | FastAPI application server  |
| SMTP / Email API | Email delivery              |
| AWS EC2          | Cloud deployment            |
| Git & GitHub     | Version control             |

---

## 📁 Project Structure

```text
ai-job-application-automation/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── jd_parser.py
│   │   ├── resume_parser.py
│   │   ├── matcher.py
│   │   ├── email_generator.py
│   │   └── email_sender.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── data/
│   ├── resume/
│   └── jobs/
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── applications.db
├── test_email.py
└── README.md
```

---

# ⚙️ Application Workflow

## 1. Job Description Processing

The system receives a job description through the FastAPI application.

Example:

```text
We are hiring a DevOps Engineer.

Required skills:
AWS
Docker
Kubernetes
Jenkins
Linux
Terraform
```

The system can process this information and prepare it for further analysis.

---

## 2. Job Information Extraction

Important information can be extracted from the job description:

```text
Job Role
Company
Required Skills
Experience
Location
HR / Recruiter Email
```

---

## 3. Resume Processing

The candidate's resume is provided as a PDF.

The application uses **PyMuPDF** to extract text from the PDF.

Example:

```text
Resume PDF
    ↓
PyMuPDF
    ↓
Extracted Resume Text
    ↓
Skills / Experience / Projects
```

---

## 4. Resume and Job Matching

The extracted resume information is compared with the job requirements.

Example:

```text
Job Requirements:

AWS          ✓
Docker       ✓
Kubernetes  ✓
Jenkins      ✓
Terraform    ✓
Python       ✓
```

The system can calculate a match percentage based on the available skills.

---

## 5. Personalized Email Generation

Based on the job description and candidate profile, the system generates a personalized application email.

Example structure:

```text
Subject:
Application for DevOps Engineer - Sanniboina Kavyasri

Dear Hiring Manager,

I am writing to apply for the DevOps Engineer position.

I have hands-on experience with AWS, Docker, Kubernetes,
Terraform, Jenkins and Linux through my DevOps learning
and project work.

Please find my resume attached for your consideration.

Regards,
Sanniboina Kavyasri
```

---

## 6. Email Sending

The generated application email can be sent through a configured email service.

The resume can be attached automatically.

```text
Generated Email
      ↓
Email Service
      ↓
HR / Recruiter
      +
Resume Attachment
```

Email credentials should **never be hard-coded** in the source code.

Use environment variables instead.

---

# 🐳 Docker

The application can be containerized using Docker.

Build the application image:

```bash
docker build -t ai-job-application-automation .
```

Run the application:

```bash
docker run -d \
  --name job-automation-app \
  -p 8000:8000 \
  ai-job-application-automation
```

Check running containers:

```bash
docker ps
```

Check application logs:

```bash
docker logs job-automation-app
```

---

# 🐳 Docker Compose

Docker Compose can be used to run the application together with PostgreSQL.

Example architecture:

```text
                 Docker Compose
                       |
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   FastAPI Container        PostgreSQL Container
       Port 8000                 Port 5432
          │                         │
          └────────────┬────────────┘
                       │
                Application Data
```

Start the services:

```bash
docker compose up -d
```

Build and start:

```bash
docker compose up --build -d
```

Check containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Stop services:

```bash
docker compose down
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_password

DATABASE_URL=postgresql://jobuser:jobpassword@postgres:5432/jobautomation
```

If an AI provider is configured:

```env
AI_API_KEY=your_api_key
```

### ⚠️ Security

Never commit `.env` to GitHub.

The repository should use:

```text
.env
```

inside `.gitignore`.

Use `.env.example` to show required variables without exposing real credentials.

---

# ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/kavyasri59/ai-job-application-automation.git
```

Enter the project:

```bash
cd ai-job-application-automation
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# 🩺 Health Check

The application provides a health endpoint:

```text
GET /health
```

Test it:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

# 📡 API

## Root Endpoint

```text
GET /
```

Example:

```bash
curl http://localhost:8000/
```

---

## Health Endpoint

```text
GET /health
```

Example:

```bash
curl http://localhost:8000/health
```

---

## Job Description Endpoint

The application can receive a job description through:

```text
POST /jobs
```

Example:

```bash
curl -X POST http://localhost:8000/jobs \
-H "Content-Type: application/json" \
-d '{
  "job_description": "We are hiring a DevOps Engineer. Required skills: AWS, Docker, Kubernetes, Jenkins and Linux."
}'
```

---

# ☁️ AWS Deployment

The application can be deployed on an Ubuntu AWS EC2 instance.

Basic deployment workflow:

```text
GitHub
   ↓
AWS EC2
   ↓
Docker
   ↓
Docker Compose
   ↓
FastAPI
   ↓
PostgreSQL
```

Example EC2 setup:

```bash
sudo apt update
sudo apt install docker.io -y
```

Check Docker:

```bash
docker --version
```

Clone the repository:

```bash
git clone https://github.com/kavyasri59/ai-job-application-automation.git
```

Enter the project:

```bash
cd ai-job-application-automation
```

Start the application:

```bash
docker compose up --build -d
```

---

# 🔄 Future Enhancements

The project can be extended with:

* AI-based job description analysis
* Resume-to-JD semantic matching
* Improved match scoring
* Job source integrations using permitted APIs/feeds
* Recruiter/HR email extraction
* Personalized application generation
* Automated email sending
* Application status tracking
* PostgreSQL database
* Web dashboard
* Authentication
* Docker Compose production setup
* AWS EC2 deployment
* Terraform infrastructure
* GitHub Actions CI/CD
* Monitoring with Prometheus and Grafana
* Application logging
* Error handling and retry mechanisms

For platforms such as LinkedIn, job-data access should use the platform's permitted APIs, feeds, or other authorized mechanisms rather than unauthorized scraping or account automation.

---

# 🔒 Security Best Practices

* Do not commit passwords.
* Do not commit API keys.
* Do not commit Gmail app passwords.
* Store secrets in environment variables or a secrets manager.
* Restrict AWS Security Group ports.
* Use HTTPS in production.
* Use strong database credentials.
* Keep `.env` out of Git.
* Rotate exposed credentials immediately.
* Use least-privilege IAM permissions on AWS.

---

# 📌 Current Project Status

| Component              | Status |
| ---------------------- | ------ |
| FastAPI application    | ✅      |
| Project structure      | ✅      |
| Health endpoint        | ✅      |
| Job description API    | ✅      |
| Resume PDF processing  | 🔄     |
| JD skill extraction    | 🔄     |
| Resume/JD matching     | 🔄     |
| Match score            | 🔄     |
| Email generation       | 🔄     |
| Email sending          | 🔄     |
| PostgreSQL integration | 🔄     |
| Docker                 | 🔄     |
| Docker Compose         | 🔄     |
| AWS deployment         | 🔄     |
| CI/CD                  | 🔜     |
| Monitoring             | 🔜     |

---

# 👩‍💻 Author

**Sanniboina Kavyasri**

DevOps / Cloud Engineer Trainee

### Skills

```text
AWS
Docker
Kubernetes
Terraform
Jenkins
Git
Linux
Python
Ansible
CI/CD
```

---



