import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Balaji R - Data Analyst/Data Engineer Resume", layout="wide")

# --- CUSTOM CSS for background and fonts ---
st.markdown("""
    <style>
        body {
            background-color: #f4f6f8;
            font-family: 'Segoe UI', sans-serif;
        }
        .css-1d391kg {
            font-size: 24px !important;
            font-weight: 600 !important;
            color: #333333 !important;
        }
        .css-10trblm {
            color: #2c3e50 !important;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stRadio > div {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.title("📂 Navigate")
sections = [
    "Profile Summary", "Professional Experience", "Key Skills",
    "Academic Projects", "Certifications & Hackathons", "Education", "Achievements"
]
selected_section = st.sidebar.radio("", sections)

# --- RESUME DOWNLOAD ---
with open("BalajiR_Resume.docx", "rb") as file:
    st.sidebar.download_button(
        label="📥 Download Resume",
        data=file,
        file_name="BalajiR_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# --- HEADER ONLY ON FIRST PAGE ---
if selected_section == "Profile Summary":
    st.title("Balaji R")
    st.markdown("""
    📍 Chennai, India  
    📞 +91 63852 16638  
    📧 balajibalaji036@gmail.com  

    🔗 [GitHub](https://github.com/Balaji036) | [Kaggle](https://www.kaggle.com/balaji036) | [LinkedIn](https://www.linkedin.com/in/balajiraja28/)
    """)

# --- CONTENT SECTIONS ---
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
    - Collaborate with multiple clients on daily basis to understand their requirements, offer strategic feedback, and deliver data in requested formats  
    - Developed and implemented an automation to address a product limitation, enabling $5.7M+ in deal closures and increasing ZoomInfo’s competitive value  
    - Deal with high-value Enterprise and Strategic accounts, contributing to renewals, up-sells, and critical new business deals  
    - Identified anomaly in Round Robin logic, led a team of 4 to redesign and successfully implement a scalable solution  
    - Appointed as Data Steward to handle critical requests, ensuring consistent delivery of accurate, high-quality data  
    - Solely handled end-to-end data and business analysis for Grafana, TeamViewer, and Employsure (Peninsula), directly supporting closed deals totaling $212K, $70K, and $194K in ACV
    """)

elif selected_section == "Key Skills":
    st.header("Key Skills")
    st.markdown("""
    - **Programming Languages:** Python, SQL, Java  
    - **Big Data & Distributed Compute:** PySpark, Databricks, Snowflake, Cyberduck  
    - **Visualization Tools:** Tableau, Excel  
    - **Data Analysis:** Data Cleaning, EDA, Business Insights, Data Storytelling  
    - **Machine Learning:** Linear Regression, Logistic Regression, Lasso, Ridge, Hypothesis Testing  
    - **Python Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, Statsmodels, Itertools  
    - **Data Querying:** DDL, DML, DQL, TCL, MySQL Workbench, PostgreSQL  
    - **Environments:** Jupyter Notebook, Visual Studio Code, Sublime Text  
    - **Enterprise Tools:** Confluence, JIRA, Salesforce, Docket AI  
    - **Professional & Soft Skills:** Client Communication, Requirement Gathering, Business Understanding, Data Interpretation, Stakeholder Collaboration, Analytical Thinking, Problem-Solving, Cross-Functional Coordination, Data-Driven Decision Making, Leadership, Adaptability, Ownership, Time Management, Attention to Detail, Agile Mindset
    """)

elif selected_section == "Academic Projects":
    st.header("Academic Projects")
    st.subheader("Project 1: Titanic Disaster - A Logistic Regression-based Survival Analysis")
    st.markdown("""
    - **Source:** Kaggle  
    - **Goal:** Examine variables that contributed to survival and use predictive modelling to predict individuals who survived the Titanic disaster  
    - Conducted data profiling to assess structure, completeness, and suitability of the dataset  
    - Built reusable data transformation modules for imputation, encoding, outlier removal, scaling, and splitting  
    - Delivered a logistic regression model with 78% accuracy  
    - **Skills:** Python, EDA, Logistic Regression, Pandas, NumPy, Matplotlib, Seaborn, Confusion Matrix, OneHotEncoder, LabelEncoder, Z-score, Standardization, OOP
    """)
    st.subheader("Project 2: Used Car Price Prediction – A Linear Regression Based Model")
    st.markdown("""
    - **Source:** Kaggle  
    - **Goal:** Build a predictive model to estimate used car prices for data-driven pricing decisions  
    - Conducted EDA, handled duplicates, outliers (Z-score), and performed feature engineering  
    - Achieved an R² of 82% and reduced MSE to 205  
    - **Skills:** Python, EDA, Linear Regression, NumPy, Pandas, Matplotlib, Seaborn, MinMaxScaler, OneHotEncoder, LabelEncoder, Z-score, OOP
    """)

elif selected_section == "Certifications & Hackathons":
    st.header("Certifications & Hackathons")
    st.markdown("""
    - GLCA Data Science Hackathon program (2023)  
    - IEEE 24 Hours Coding Marathon Program (2019 & 2020)  
    - HackerRank SQL Gold badge  
    - Apache PySpark By Example  
    - Tableau Essential Training  
    - SQL For Data Analysis, Intermediate SQL For Data Scientist
    """)

elif selected_section == "Education":
    st.header("Education")
    st.markdown("""
    - **Data Analytics**, Great Lakes Institute of Management – *2023* (Completed)  
    - **B.E. Computer Science Engineering**, Panimalar Engineering College – *2022* (89.60%)  
    - **12th Grade**, St. Joseph of Cluny MHSS – *2018* (87.3%)  
    - **10th Grade**, St. Joseph of Cluny MHSS – *2016* (96%)
    """)

elif selected_section == "Achievements":
    st.header("Achievements")
    st.markdown("""
    - Dream Winner – Q2 2024, ZoomInfo (Top Performer of the Quarter)  
    - 5× New Business Star – Honored in Revenue All Hands for consistent top-tier performance
    """)
