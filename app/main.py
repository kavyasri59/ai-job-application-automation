from app.services.job_database import save_job, get_all_jobs
from app.database.database import create_tables
from app.services.job_source import fetch_jobs
from fastapi.responses import HTMLResponse 
from app.services.message_generator import generate_hr_message 
from app.services.resume_generator import generate_custom_resume 
from app.services.email_sender import send_email 
from fastapi import FastAPI, UploadFile, File, HTTPException 
from pydantic import BaseModel 
import os 
 
from app.config import APP_NAME 
from app.services.jd_parser import analyze_job_description 
from app.services.resume_parser import analyze_resume 
from app.services.job_matcher import calculate_match 
 
 
app = FastAPI( 
    title=APP_NAME, 
    description="AI-powered job application automation system", 
    version="1.0.0" 
) 
create_tables()
@app.get("/jobs")
def get_jobs():
    jobs = fetch_jobs()

    for job in jobs:
        save_job(job)

    stored_jobs = get_all_jobs()

    return {
        "status": "success",
        "count": len(stored_jobs),
        "jobs": stored_jobs
    }
 
 
class JobDescriptionRequest(BaseModel): 
    job_description: str 
 
 
class MatchJobRequest(BaseModel): 
    job_description: str 
    resume_filename: str 
 
 
@app.get("/", response_class=HTMLResponse) 
def root(): 
    return """ 
    <!DOCTYPE html> 
    <html> 
    <head> 
        <title>AI Job Application Automation</title> 
 
        <style> 
            * { 
                box-sizing: border-box; 
            } 
 
            body { 
                font-family: Arial, sans-serif; 
                background: #f4f6f8; 
                margin: 0; 
                padding: 0; 
            } 
 
            .container { 
                width: 90%; 
                max-width: 1000px; 
                margin: 40px auto; 
                background: white; 
                padding: 35px; 
                border-radius: 15px; 
                box-shadow: 0 4px 20px rgba(0,0,0,0.1); 
            } 
 
            h1 { 
                text-align: center; 
                color: #1f2937; 
            } 
 
            .subtitle { 
                text-align: center; 
                color: #666; 
                margin-bottom: 35px; 
            } 
 
            .section { 
                margin-bottom: 25px; 
            } 
 
            label { 
                display: block; 
                font-weight: bold; 
                margin-bottom: 8px; 
                color: #333; 
            } 
 
            textarea { 
                width: 100%; 
                min-height: 180px; 
                padding: 12px; 
                border: 1px solid #ccc; 
                border-radius: 8px; 
                font-size: 15px; 
                resize: vertical; 
            } 
 
            input[type="text"], 
            input[type="email"], 
            input[type="file"] { 
                width: 100%; 
                padding: 12px; 
                border: 1px solid #ccc; 
                border-radius: 8px; 
                font-size: 15px; 
            } 
 
            button { 
                background: #2563eb; 
                color: white; 
                border: none; 
                padding: 12px 22px; 
                border-radius: 8px; 
                cursor: pointer; 
                font-size: 15px; 
                margin: 5px; 
            } 
 
            button:hover { 
                background: #1d4ed8; 
            } 
 
            .result { 
                background: #f8fafc; 
                border: 1px solid #ddd; 
                border-radius: 8px; 
                padding: 20px; 
                margin-top: 15px; 
                white-space: pre-wrap; 
            } 
 
            .success { 
                color: #047857; 
                font-weight: bold; 
            } 
 
            .error { 
                color: #dc2626; 
                font-weight: bold; 
            } 
 
            .grid { 
                display: grid; 
                grid-template-columns: 1fr 1fr; 
                gap: 20px; 
            } 
 
            @media(max-width: 700px) { 
                .grid { 
                    grid-template-columns: 1fr; 
                } 
            } 
        </style> 
    </head> 
 
    <body> 
 
    <div class="container"> 
 
        <h1>AI Job Application Automation</h1> 
 
        <p class="subtitle"> 
            Analyze jobs, match your resume, generate a customized resume 
            and create an HR message. 
        </p> 
 
 
        <!-- JOB DESCRIPTION --> 
 
        <div class="section"> 
 
            <label>1. Job Description</label> 
 
            <textarea 
                id="jobDescription" 
                placeholder="Paste the complete job description here..." 
            ></textarea> 
 
            <button onclick="analyzeJob()"> 
                Analyze Job 
            </button> 
 
            <div id="jobResult" class="result"></div> 
 
        </div> 
 
 
        <!-- RESUME --> 
 
        <div class="section"> 
 
            <label>2. Upload Resume</label> 
 
            <input 
                type="file" 
                id="resumeFile" 
                accept=".pdf" 
            > 
 
            <button onclick="uploadResume()"> 
                Upload & Analyze Resume 
            </button> 
 
            <div id="resumeResult" class="result"></div> 
 
        </div> 
 
 
        <!-- MATCH --> 
 
        <div class="section"> 
 
            <button onclick="matchJob()"> 
                Match Job & Resume 
            </button> 
 
            <div id="matchResult" class="result"></div> 
 
        </div> 
 
 
        <!-- CANDIDATE DETAILS --> 
 
        <div class="section"> 
 
            <h2>Candidate Details</h2> 
 
            <div class="grid"> 
 
                <div> 
                    <label>Name</label> 
                    <input 
                        type="text" 
                        id="candidateName" 
                        value="Sanniboina Kavyasri" 
                    > 
                </div> 
 
                <div> 
                    <label>Email</label> 
                    <input 
                        type="email" 
                        id="candidateEmail" 
                        value="kavyasrisanniboina@gmail.com" 
                    > 
                </div> 
 
                <div> 
                    <label>Phone</label> 
                    <input 
                        type="text" 
                        id="candidatePhone" 
                        placeholder="Enter phone number" 
                    > 
                </div> 
 
                <div> 
                    <label>GitHub</label> 
                    <input 
                        type="text" 
                        id="candidateGithub" 
                        value="github.com/kavyasri59" 
                    > 
                </div> 
 
                <div> 
                    <label>LinkedIn</label> 
                    <input 
                        type="text" 
                        id="candidateLinkedin" 
                        placeholder="LinkedIn profile" 
                    > 
                </div> 
 
                <div> 
                    <label>Company Name</label> 
                    <input 
                        type="text" 
                        id="companyName" 
                        placeholder="Company name" 
                    > 
                </div> 
 
            </div> 
 
        </div> 
 
 
        <!-- GENERATE RESUME --> 
 
        <div class="section"> 
 
            <button onclick="generateResume()"> 
                Generate Customized Resume 
            </button> 
 
            <div id="resumeGenerateResult" class="result"></div> 
 
        </div> 
 
 
        <!-- HR MESSAGE --> 
 
        <div class="section"> 
 
            <label>HR Name</label> 
 
            <input 
                type="text" 
                id="hrName" 
                value="Hiring Manager" 
            > 
 
            <button onclick="generateMessage()"> 
                Generate HR Message 
            </button> 
 
            <div id="messageResult" class="result"></div> 
 
        </div> 
 
    </div> 
 
 
    <script> 
 
        let uploadedResumeFilename = ""; 
        let resumeText = ""; 
        let matchData = {}; 
 
 
        async function analyzeJob() { 
 
            const jobDescription = 
                document.getElementById("jobDescription").value; 
 
            if (!jobDescription.trim()) { 
                alert("Please paste the job description."); 
                return; 
            } 
 
            const response = await fetch("/analyze-job", { 
                method: "POST", 
 
                headers: { 
                    "Content-Type": "application/json" 
                }, 
 
                body: JSON.stringify({ 
                    job_description: jobDescription 
                }) 
            }); 
 
            const data = await response.json(); 
 
            document.getElementById("jobResult").innerHTML = 
                "<b>Job Title:</b> " + (data.job_title || "Not detected") + 
                "<br><br>" + 
                "<b>Experience:</b> " + (data.experience || "Not detected") + 
                "<br><br>" + 
                "<b>Location:</b> " + (data.location || "Not detected") + 
                "<br><br>" + 
                "<b>Skills:</b> " + 
                (data.skills || []).join(", "); 
        } 
 
 
        async function uploadResume() { 
 
            const file = 
                document.getElementById("resumeFile").files[0]; 
 
            if (!file) { 
                alert("Please select your PDF resume."); 
                return; 
            } 
 
            const formData = new FormData(); 
 
            formData.append("file", file); 
 
            const response = await fetch("/upload-resume", { 
                method: "POST", 
                body: formData 
            }); 
 
            const data = await response.json(); 
 
            if (!response.ok) { 
                document.getElementById("resumeResult").innerHTML = 
                    "<span class='error'>" + 
                    (data.detail || "Resume upload failed") + 
                    "</span>"; 
                return; 
            } 
 
            uploadedResumeFilename = data.filename; 
            resumeText = data.resume_text || ""; 
 
            document.getElementById("resumeResult").innerHTML = 
                "<span class='success'>Resume uploaded successfully.</span>" + 
                "<br><br>" + 
                "<b>Detected Skills:</b> " + 
                data.skills.join(", "); 
        } 
 
 
        async function matchJob() { 
 
            const jobDescription = 
                document.getElementById("jobDescription").value; 
 
            if (!jobDescription.trim()) { 
                alert("Please enter the job description."); 
                return; 
            } 
 
            if (!uploadedResumeFilename) { 
                alert("Please upload your resume first."); 
                return; 
            } 
 
            const response = await fetch("/match-job", { 
                method: "POST", 
 
                headers: { 
                    "Content-Type": "application/json" 
                }, 
 
                body: JSON.stringify({ 
                    job_description: jobDescription, 
                    resume_filename: uploadedResumeFilename 
                }) 
            }); 
 
            const data = await response.json(); 
 
            if (!response.ok) { 
                document.getElementById("matchResult").innerHTML = 
                    "<span class='error'>" + 
                    (data.detail || "Matching failed") + 
                    "</span>"; 
                return; 
            } 
 
            matchData = data; 
 
            document.getElementById("matchResult").innerHTML = 
                "<b>Job Title:</b> " + data.job_title + 
                "<br><br>" + 
                "<b>Match Percentage:</b> " + 
                data.match_percentage + "%" + 
                "<br><br>" + 
                "<b>Matched Skills:</b> " + 
                data.matched_skills.join(", ") + 
                "<br><br>" + 
                "<b>Missing Skills:</b> " + 
                data.missing_skills.join(", "); 
        } 
 
 
        async function generateResume() { 
 
            if (!matchData.matched_skills) { 
                alert("Please match the job and resume first."); 
                return; 
            } 
 
            const requestData = { 
 
                name: 
                    document.getElementById("candidateName").value, 
 
                email: 
                    document.getElementById("candidateEmail").value, 
 
                phone: 
                    document.getElementById("candidatePhone").value, 
 
                github: 
                    document.getElementById("candidateGithub").value, 
 
                linkedin: 
                    document.getElementById("candidateLinkedin").value, 
 
                job_title: 
                    matchData.job_title || "DevOps Engineer", 
 
                matched_skills: 
                    matchData.matched_skills, 
 
                resume_text: 
                    resumeText 
            }; 
 
 
            const response = await fetch("/generate-resume", { 
 
                method: "POST", 
 
                headers: { 
                    "Content-Type": "application/json" 
                }, 
 
                body: JSON.stringify(requestData) 
 
            }); 
 
 
            const data = await response.json(); 
 
 
            document.getElementById("resumeGenerateResult").innerHTML = 
                "<span class='success'>" + 
                data.message + 
                "</span>" + 
                "<br><br>" + 
                "Generated file: " + 
                data.resume_path; 
        } 
 
 
        async function generateMessage() { 
 
    if (!matchData.matched_skills) { 
        alert("Please match the job and resume first."); 
        return; 
    } 
 
    const requestData = { 
 
        candidate_name: 
            document.getElementById("candidateName").value, 
 
        job_title: 
            matchData.job_title || "DevOps Engineer", 
 
        company_name: 
            document.getElementById("companyName").value, 
 
        matched_skills: 
            matchData.matched_skills, 
 
        hr_name: 
            document.getElementById("hrName").value 
 
    }; 
 
    if (!requestData.company_name) { 
        alert("Please enter the company name."); 
        return; 
    } 
 
    const response = await fetch("/generate-message", { 
 
        method: "POST", 
 
        headers: { 
            "Content-Type": "application/json" 
        }, 
 
        body: JSON.stringify(requestData) 
 
    }); 
 
    const result = await response.json(); 
 
    if (!response.ok) { 
        alert(result.detail || "Failed to generate HR message."); 
        return; 
    } 
 
    // Automatically fill Email Subject 
    document.getElementById("email_subject").value = 
        result.subject || ""; 
 
    // Automatically fill Email Message 
    document.getElementById("email_body").value = 
        result.message || ""; 
 
    alert("HR message generated successfully!"); 
} 
 
    </script> 
<hr> 
 
<h2>📧 Send Job Application</h2> 
 
<label>HR Email:</label><br> 
<input 
    type="email" 
    id="recipient_email" 
    placeholder="hr@company.com" 
    style="width:400px;padding:8px;" 
> 
<br><br> 
 
<label>Email Subject:</label><br> 
<input 
    type="text" 
    id="email_subject" 
    placeholder="Application for DevOps Engineer" 
    style="width:400px;padding:8px;" 
> 
<br><br> 
 
<label>Email Message:</label><br> 
<textarea 
    id="email_body" 
    rows="10" 
    style="width:600px;padding:10px;" 
    placeholder="Dear Hiring Manager..." 
></textarea> 
<br><br> 
 
<label>Resume:</label><br> 
 
<input 
    type="text" 
    id="attachment_path" 
    value="generated_resumes/customized_resume.pdf" 
    style="width:400px;padding:8px;" 
    readonly 
> 
<br><br> 
 
<button onclick="sendApplication()"> 
    📧 Send Application 
</button> 
 
<pre id="email_result"></pre> 
 
<script> 
 
async function sendApplication() { 
 
    const recipient_email = 
        document.getElementById("recipient_email").value; 
 
    const subject = 
        document.getElementById("email_subject").value; 
 
    const body = 
        document.getElementById("email_body").value; 
 
    const attachment_path = 
        document.getElementById("attachment_path").value; 
 
    if (!recipient_email) { 
        alert("Please enter HR email"); 
        return; 
    } 
 
    if (!subject) { 
        alert("Please enter email subject"); 
        return; 
    } 
 
    if (!body) { 
        alert("Please enter email message"); 
        return; 
    } 
 
    const response = await fetch("/send-email", { 
 
        method: "POST", 
 
        headers: { 
            "Content-Type": "application/json" 
        }, 
 
        body: JSON.stringify({ 
            recipient_email: recipient_email, 
            subject: subject, 
            body: body, 
            attachment_path: attachment_path 
        }) 
    }); 
 
    const result = await response.json(); 
 
    document.getElementById("email_result").textContent = 
        JSON.stringify(result, null, 2); 
} 
 
</script> 
 
    </body> 
    </html> 
    """ 
     
@app.get("/health") 
def health(): 
    return { 
        "status": "healthy" 
    } 
 
 
@app.post("/analyze-job") 
def analyze_job(request: JobDescriptionRequest): 
 
    result = analyze_job_description( 
        request.job_description 
    ) 
 
    return result 
 
 
@app.post("/upload-resume") 
async def upload_resume(file: UploadFile = File(...)): 
 
    if not file.filename.lower().endswith(".pdf"): 
        raise HTTPException( 
            status_code=400, 
            detail="Only PDF files are allowed" 
        ) 
 
    os.makedirs("resumes", exist_ok=True) 
 
    file_path = os.path.join( 
        "resumes", 
        file.filename 
    ) 
 
    contents = await file.read() 
 
    with open(file_path, "wb") as f: 
        f.write(contents) 
 
    result = analyze_resume(file_path) 
 
    return { 
    "filename": file.filename, 
    "skills": result["skills"], 
    "resume_text": result["text"], 
    "message": "Resume uploaded and analyzed successfully" 
} 
 
 
@app.post("/match-job") 
def match_job(request: MatchJobRequest): 
 
    resume_path = os.path.join( 
        "resumes", 
        request.resume_filename 
    ) 
 
    if not os.path.exists(resume_path): 
        raise HTTPException( 
            status_code=404, 
            detail="Resume not found" 
        ) 
 
    job_result = analyze_job_description( 
        request.job_description 
    ) 
 
    resume_result = analyze_resume( 
        resume_path 
    ) 
 
    match_result = calculate_match( 
        job_result["skills"], 
        resume_result["skills"] 
    ) 
 
    return { 
        "job_title": job_result["job_title"], 
        "experience": job_result["experience"], 
        "location": job_result["location"], 
        "job_skills": job_result["skills"], 
        "resume_skills": resume_result["skills"], 
        "match_percentage": match_result["match_percentage"], 
        "matched_skills": match_result["matched_skills"], 
        "missing_skills": match_result["missing_skills"] 
    } 
 
 
@app.post("/generate-resume") 
def generate_resume(request: dict): 
 
    output_path = "generated_resumes/customized_resume.pdf" 
 
    matched_skills = request.get("matched_skills", []) 
 
    resume_text = request.get( 
        "resume_text", 
        "" 
    ) 
 
    result = generate_custom_resume( 
        output_path=output_path, 
        name=request.get( 
            "name", 
            "Sanniboina Kavyasri" 
        ), 
        email=request.get( 
            "email", 
            "" 
        ), 
        phone=request.get( 
            "phone", 
            "" 
        ), 
        github=request.get( 
            "github", 
            "github.com/kavyasri59" 
        ), 
        linkedin=request.get( 
            "linkedin", 
            "" 
        ), 
        job_title=request.get( 
            "job_title", 
            "DevOps Engineer" 
        ), 
        matched_skills=matched_skills, 
        resume_text=resume_text 
    ) 
 
    return { 
        "message": "Customized resume generated successfully", 
        "resume_path": result 
    } 
@app.post("/generate-message") 
def generate_message(request: dict): 
 
    result = generate_hr_message( 
        candidate_name=request["candidate_name"], 
        job_title=request["job_title"], 
        company_name=request["company_name"], 
        matched_skills=request["matched_skills"], 
        hr_name=request.get("hr_name", "Hiring Manager") 
    ) 
 
    return result 
@app.post("/send-email") 
def send_application_email(request: dict): 
    result = send_email( 
        recipient_email=request["recipient_email"], 
        subject=request["subject"], 
        body=request["body"], 
        attachment_path=request.get("attachment_path") 
    ) 
 
    return result 
