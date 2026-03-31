# Simple Skill Gap Analyzer (Basic Version)

resume_skills = ["python", "sql", "communication"]
job_skills = ["python", "machine learning", "sql", "data analysis"]

missing_skills = []

for skill in job_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)

print("Missing Skills:", missing_skills)
