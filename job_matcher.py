import csv
import os


def recommend_roles(skills, top_n=5):

    csv_path = os.path.join("data", "job_roles.csv")
    recommendations = []

    # Read roles from CSV
    if os.path.exists(csv_path):
        try:
            with open(csv_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:

                    role = (
                        row.get("role")
                        or row.get("Role")
                        or row.get("job_role")
                        or row.get("Job Role")
                        or "Unknown Role"
                    )

                    role_skills_text = (
                        row.get("skills")
                        or row.get("Skills")
                        or row.get("required_skills")
                        or ""
                    )

                    required_skills = [
                        s.strip()
                        for s in role_skills_text.split(",")
                        if s.strip()
                    ]

                    matched_skills = []
                    missing_skills = []

                    for required in required_skills:

                        found = False

                        for skill in skills:
                            if skill.lower() == required.lower():
                                matched_skills.append(skill)
                                found = True
                                break

                        if not found:
                            missing_skills.append(required)

                    if matched_skills or required_skills:

                        score = 0

                        if required_skills:
                            score = round(
                                (len(matched_skills) / len(required_skills)) * 100
                            )

                        recommendations.append({
                            "role": role,
                            "matched": matched_skills,
                            "matched_skills": matched_skills,
                            "skills": matched_skills,
                            "missing": missing_skills,
                            "score": score,
                            "match": score
                        })

        except Exception:
            recommendations = []

    # Default roles
    if not recommendations:

        default_roles = {
            "Python Developer": [
                "python",
                "flask",
                "django",
                "sql"
            ],

            "Data Scientist": [
                "python",
                "machine learning",
                "pandas",
                "numpy",
                "data science"
            ],

            "Machine Learning Engineer": [
                "python",
                "machine learning",
                "tensorflow",
                "keras",
                "pytorch"
            ],

            "Web Developer": [
                "html",
                "css",
                "javascript",
                "react"
            ],

            "Data Analyst": [
                "python",
                "sql",
                "excel",
                "power bi",
                "data analysis"
            ]
        }

        for role, required_skills in default_roles.items():

            matched_skills = []
            missing_skills = []

            for required in required_skills:

                found = False

                for skill in skills:
                    if skill.lower() == required.lower():
                        matched_skills.append(skill)
                        found = True
                        break

                if not found:
                    missing_skills.append(required)

            score = round(
                (len(matched_skills) / len(required_skills)) * 100
            )

            recommendations.append({
                "role": role,
                "matched": matched_skills,
                "matched_skills": matched_skills,
                "skills": matched_skills,
                "missing": missing_skills,
                "score": score,
                "match": score
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:top_n]