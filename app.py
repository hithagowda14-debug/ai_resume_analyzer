import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import recommend_roles
from roadmap_generator import generate_roadmap


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write(
    "Upload your resume to analyze your skills, "
    "find suitable job roles, identify skill gaps, "
    "and generate a learning roadmap."
)


uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    try:

        # Extract text
        resume_text = extract_resume_text(uploaded_file)

        # Clean text
        cleaned_text = clean_text(resume_text)

        # Extract skills
        skills = extract_skills(cleaned_text)

        st.header("🔎 Extracted Skills")

        if skills:

            st.write(", ".join(skills))

        else:

            st.warning(
                "No known skills were detected."
            )


        # Recommendations
        results = recommend_roles(skills)

        st.header("💼 Job Recommendations")


        for result in results[:3]:

            st.subheader(result["role"])

            st.progress(
                int(result["score"])
            )

            st.write(
                f"Match Score: {result['score']}%"
            )


        # Target role
        roles = [result["role"] for result in results]

        selected_role = st.selectbox(
            "Select a target role",
            roles
        )


        selected_result = next(
            result
            for result in results
            if result["role"] == selected_role
        )


        st.header("📊 Match Analysis")

        st.metric(
            "Match Score",
            f"{selected_result['score']}%"
        )


        st.subheader("✅ Skills Found")

        if selected_result["matched"]:

            for skill in selected_result["matched"]:

                st.write(f"✓ {skill}")

        else:

            st.write("No matching skills found.")


        st.subheader("❌ Missing Skills")

        missing_skills = selected_result["missing"]

        if missing_skills:

            for skill in missing_skills:

                st.write(f"• {skill}")

        else:

            st.success(
                "No major missing skills detected!"
            )


        # Roadmap
        st.header("📚 Learning Roadmap")

        roadmap = generate_roadmap(
            missing_skills
        )

        for item in roadmap:

            st.subheader(
                item["skill"]
            )

            for topic in item["topics"]:

                st.write(
                    f"→ {topic}"
                )


    except Exception as e:

        st.error(
            f"Error processing resume: {e}"
        )