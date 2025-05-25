import streamlit as st

# Page config
st.set_page_config(page_title="Balaji R - Resume", layout="wide")

# Sidebar for navigation
sections = [
    "Profile Summary", "Professional Experience", "Key Skills",
    "Academic Projects", "Certifications & Hackathons", "Education", "Achievements"
]
st.sidebar.title("Navigate")
selected_section = st.sidebar.radio("Go to", sections)

# Downloadable resume file
with open("BalajiR_Resume_for_Download.docx", "rb") as file:
    st.sidebar.download_button(
        label="📥 Download Resume (DOCX)",
        data=file,
        file_name="BalajiR_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Header section
st.title("Balaji R")
st.write("📍 Chennai, India | 📞 +91 63852 16638 | 📧 balajibalaji036@gmail.com")
st.write("[GitHub](https://github.com/Balaji036) | [Kaggle](https://www.kaggle.com/balaji036) | [LinkedIn](https://www.linkedin.com/in/balajiraja28/)")

# Content sections
if selected_section == "Profile Summary":
    st.header("Profile Summary")
    st.write("""
    Strategic and detail-oriented Data Analyst with 2+ years of experience delivering data-backed insights that drive business performance and client success. 
    Skilled at understanding complex business contexts, identifying opportunities through data, and communicating insights with clarity and confidence. 
    I bring a consulting mindset to every project—thinking beyond the immediate ask, aligning with business goals, and building trust through accuracy, ownership, and thoughtful analysis.
    Passionate about solving real-world problems in fast-paced, impact-driven environments.
    """)

elif selected_section == "Professional Experience":
    st.header("Professional Experience")
    st.subheader("ZoomInfo Technologies | Data Analyst I")
    st.write("**June 2023 – Present | Chennai, India**")
    st.markdown("""
    - Collaborate with clients to understand requirements and deliver tailored data solutions  
    - Built automation enabling $5.7M+ in deal closures  
    - Led fix for Round Robin logic with team of 4  
    - Managed enterprise/strategic accounts, supporting renewals and up-sells  
    - Appointed Data Steward for critical requests  
    - Solely handled end-to-end analysis for Grafana, TeamViewer, Employsure (ACVs: $212K, $70K, $194K)
    """)

elif selected_section == "Key Skills":
    st.header("Key Skills")
    st.markdown("""
    - **Languages & Tools:** Python, SQL, Java  
    - **Big Data:** PySpark, Databricks, Snowflake  
    - **Visualization:** Tableau, Excel  
    - **Data Analysis:** EDA, Data Cleaning, Storytelling  
    - **ML Techniques:** Regression, Hypothesis Testing  
    - **Libraries:** Pandas, NumPy, Seaborn, Scikit-learn  
    - **Databases:** MySQL, PostgreSQL  
    - **Tools:** Jupyter, VS Code, Salesforce, JIRA  
    - **Soft Skills:** Communication, Ownership, Agile mindset
    """)

elif selected_section == "Academic Projects":
    st.header("Academic Projects")
    st.subheader("1. Titanic Survival Prediction")
    st.markdown("""
    - Built a logistic regression model with 78% accuracy  
    - Performed EDA, feature engineering, and model tuning  
    - Tools: Python, Pandas, Seaborn, OOP
    """)
    st.subheader("2. Used Car Price Prediction")
    st.markdown("""
    - Built a linear regression model (82% R², low MSE)  
    - Conducted outlier removal, normalization, iterative tuning  
    - Tools: Python, Pandas, MinMaxScaler
    """)

elif selected_section == "Certifications & Hackathons":
    st.header("Certifications & Hackathons")
    st.markdown("""
    - GLCA Data Science Hackathon (2023)  
    - IEEE 24-Hour Coding Marathon (2019 & 2020)  
    - HackerRank SQL Gold Badge  
    - Apache PySpark By Example  
    - Tableau Essential Training  
    - SQL for Data Analysis
    """)

elif selected_section == "Education":
    st.header("Education")
    st.markdown("""
    - **Data Analytics**, Great Lakes Institute of Management – *2023*  
    - **B.E. Computer Science**, Panimalar Engineering College – *2022 (89.60%)*  
    - **12th Grade**, St. Joseph of Cluny – *2018 (87.3%)*  
    - **10th Grade**, St. Joseph of Cluny – *2016 (96%)*  
    """)

elif selected_section == "Achievements":
    st.header("Achievements")
    st.markdown("""
    - Dream Winner – Q2 2024 (Top Performer of the Quarter)  
    - 5× New Business Star – Recognized in ZoomInfo Revenue All Hands
    """)

