from job_board.models import JobPosting

#for filling the database

jobs = [
    {
        "title": "Software Engineer",
        "description": "Develop backend services and APIs.",
        "company": "TechNova",
        "salary": 95000,
        "is_active": True
    },
    {
        "title": "Data Analyst",
        "description": "Analyze business data and create dashboards.",
        "company": "InsightWorks",
        "salary": 70000,
        "is_active": True
    },
    {
        "title": "Marketing Coordinator",
        "description": "Assist with marketing campaigns and social media.",
        "company": "BrandBoost",
        "salary": 50000,
        "is_active": False
    },
    {
        "title": "Project Manager",
        "description": "Oversee software development projects.",
        "company": "AgileFlow",
        "salary": 85000,
        "is_active": True
    },
    {
        "title": "HR Generalist",
        "description": "Handle recruitment, onboarding, and HR operations.",
        "company": "PeopleFirst",
        "salary": 60000,
        "is_active": False
    },
]

for job in jobs:
    JobPosting.objects.create(**job)

print("Database seeded successfully!")
