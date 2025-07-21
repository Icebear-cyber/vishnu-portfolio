import streamlit as st

st.title("🛠️ Skills")

st.write("Here are some of the tools, technologies, and languages I'm confident in:")

skills = {
    "💻 Programming Languages": ["Python", "C", "C++ (Basics)", "SQL"],
    "📦 Libraries & Frameworks": ["Streamlit", "Pandas", "OpenPyXL", "Regex", "Scikit-learn (Basic)"],
    "🔧 Tools": ["VS Code", "Git & GitHub", "Jupyter Notebook", "Power BI"],
    "🌐 Soft Skills": ["Problem Solving", "Fast Learner", "Communication", "Self-driven"]
}

for category, items in skills.items():
    st.subheader(category)
    st.write("• " + "\n• ".join(items))
