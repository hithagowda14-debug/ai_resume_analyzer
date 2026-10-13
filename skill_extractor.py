import re


def extract_skills(text):
    """
    Extract common technical and soft skills from resume text.
    """

    skills_list = [
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "html",
        "css",
        "react",
        "node.js",
        "sql",
        "mysql",
        "mongodb",
        "flask",
        "django",
        "streamlit",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "data analysis",
        "tensorflow",
        "keras",
        "pytorch",
        "pandas",
        "numpy",
        "scikit-learn",
        "git",
        "github",
        "power bi",
        "excel",
        "communication",
        "leadership",
        "problem solving",
        "teamwork"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills