from flask import Flask, render_template, request, redirect, url_for
from matcher import get_best_matches

app = Flask(__name__)

INTERNSHIPS = [
    {
        "company": "Tech Corp",
        "role": "Backend Python Developer Intern",
        "required_skills": ["python", "flask", "sql", "git"],
        "location": "Chennai, Tamil Nadu",
        "work_mode": "Hybrid",
        "duration": "3 Months",
        "stipend": "₹18,000 / month"
    },
    {
        "company": "DataWorks",
        "role": "Data Analyst Intern",
        "required_skills": ["python", "pandas", "sql", "excel"],
        "location": "Bengaluru, Karnataka",
        "work_mode": "Hybrid",
        "duration": "3 Months",
        "stipend": "₹20,000 / month"
    },
    {
        "company": "Web Solutions",
        "role": "Frontend Web Developer Intern",
        "required_skills": ["html", "css", "javascript", "bootstrap"],
        "location": "Remote",
        "work_mode": "Remote",
        "duration": "2 Months",
        "stipend": "₹12,000 / month"
    },
    {
        "company": "Cloud Sync",
        "role": "Cloud & DevOps Intern",
        "required_skills": ["python", "linux", "aws", "docker"],
        "location": "Hyderabad, Telangana",
        "work_mode": "On-site",
        "duration": "6 Months",
        "stipend": "₹25,000 / month"
    },
    {
        "company": "NexaAI Labs",
        "role": "Machine Learning & NLP Intern",
        "required_skills": ["python", "pytorch", "machine learning", "nlp"],
        "location": "Bengaluru, Karnataka",
        "work_mode": "Hybrid",
        "duration": "6 Months",
        "stipend": "₹30,000 / month"
    },
    {
        "company": "SecureNet Systems",
        "role": "Cybersecurity & Linux Intern",
        "required_skills": ["linux", "networking", "python", "cybersecurity"],
        "location": "Chennai, Tamil Nadu",
        "work_mode": "On-site",
        "duration": "3 Months",
        "stipend": "₹16,000 / month"
    },
    {
        "company": "PixelCraft Studio",
        "role": "Full-Stack React & Node Intern",
        "required_skills": ["javascript", "react", "node.js", "mongodb", "css"],
        "location": "Remote",
        "work_mode": "Remote",
        "duration": "3 Months",
        "stipend": "₹15,000 / month"
    },
    {
        "company": "FinPulse Technologies",
        "role": "Software Engineering Intern (APIs)",
        "required_skills": ["python", "fastapi", "postgresql", "docker", "git"],
        "location": "Mumbai, Maharashtra",
        "work_mode": "Hybrid",
        "duration": "6 Months",
        "stipend": "₹28,000 / month"
    },
    {
        "company": "AppForge Mobility",
        "role": "Android & Flutter App Intern",
        "required_skills": ["dart", "flutter", "firebase", "git"],
        "location": "Pune, Maharashtra",
        "work_mode": "Remote",
        "duration": "3 Months",
        "stipend": "₹14,000 / month"
    },
    {
        "company": "InsightGrid Analytics",
        "role": "Business Intelligence Intern",
        "required_skills": ["sql", "power bi", "excel", "python"],
        "location": "Chennai, Tamil Nadu",
        "work_mode": "On-site",
        "duration": "3 Months",
        "stipend": "₹15,000 / month"
    },
    {
        "company": "RoboCore Automation",
        "role": "Embedded & C++ Software Intern",
        "required_skills": ["c++", "c", "linux", "git"],
        "location": "Coimbatore, Tamil Nadu",
        "work_mode": "On-site",
        "duration": "6 Months",
        "stipend": "₹18,000 / month"
    },
    {
        "company": "TestSphere QA",
        "role": "Software Automation & QA Intern",
        "required_skills": ["python", "pytest", "selenium", "git"],
        "location": "Remote",
        "work_mode": "Remote",
        "duration": "2 Months",
        "stipend": "₹12,000 / month"
    }
]


@app.route("/", methods=["GET"])
def index():
    top_companies = [
        {"name": item["company"], "skills": item["required_skills"]}
        for item in INTERNSHIPS[:6]
    ]
    return render_template("index.html", top_companies=top_companies)


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        return redirect(url_for("index"))

    raw_skills = request.form.get("skills", "")
    skills_list = [s.strip() for s in raw_skills.split(",") if s.strip()]

    student = {
        "name": request.form.get("name", "").strip(),
        "email": request.form.get("email", "").strip(),
        "phone": request.form.get("phone", "").strip(),
        "address": request.form.get("address", "").strip(),
        "degree": request.form.get("degree", "").strip(),
        "year": request.form.get("year", "").strip(),
        "work_mode": request.form.get("work_mode", "Any").strip(),
        "duration": request.form.get("duration", "").strip(),
        "portfolio": request.form.get("portfolio", "").strip(),
        "bio": request.form.get("bio", "").strip(),
        "skills": skills_list,
        "skills_list": skills_list,
    }

    matches = get_best_matches(student, INTERNSHIPS)

    preferred_mode = student["work_mode"].lower()
    if preferred_mode != "any":
        matches.sort(
            key=lambda x: (
                x["match_score"],
                1 if x.get("work_mode", "").lower() == preferred_mode else 0
            ),
            reverse=True
        )

    return render_template("results.html", student=student, matches=matches)


if __name__ == "__main__":
    app.run(debug=True)
