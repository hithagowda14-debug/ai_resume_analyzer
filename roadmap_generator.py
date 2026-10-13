ROADMAP = {

    "Python": [
        "Learn Python fundamentals",
        "Practice functions and OOP",
        "Build small Python projects"
    ],

    "SQL": [
        "Learn SQL basics",
        "Practice SELECT and JOIN queries",
        "Work with databases"
    ],

    "Machine Learning": [
        "Learn supervised and unsupervised learning",
        "Study regression and classification",
        "Build ML projects using scikit-learn"
    ],

    "Scikit-learn": [
        "Learn preprocessing",
        "Learn model training",
        "Practice model evaluation"
    ],

    "FastAPI": [
        "Learn REST APIs",
        "Create a FastAPI application",
        "Deploy an ML model using FastAPI"
    ],

    "Docker": [
        "Learn Docker fundamentals",
        "Create a Dockerfile",
        "Containerize a Python application"
    ],

    "Power BI": [
        "Learn Power BI basics",
        "Create dashboards",
        "Practice data visualization"
    ],

    "NLP": [
        "Learn text preprocessing",
        "Study NLP techniques",
        "Build an NLP project"
    ],

    "Deep Learning": [
        "Learn neural networks",
        "Study CNN and RNN",
        "Build a deep learning project"
    ]
}


def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        if skill in ROADMAP:

            roadmap.append({
                "skill": skill,
                "topics": ROADMAP[skill]
            })

        else:

            roadmap.append({
                "skill": skill,
                "topics": [
                    f"Learn {skill} fundamentals",
                    f"Practice {skill} with projects"
                ]
            })

    return roadmap