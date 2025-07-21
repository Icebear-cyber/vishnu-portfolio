import streamlit as st
from PIL import Image

# Load profile image
img = Image.open("assets/profile.jpg")

# Set wide layout
st.set_page_config(layout="wide", page_title="Vishnu Portfolio")

# ----- HEADER -----
col1, col2 = st.columns([1, 2])

with col1:
    st.image(img, width=200)

with col2:
    st.title("Vishnu Vardhan Dumpala")
    st.subheader("Python Developer | Automation Enthusiast | Cybersecurity Learner")
    st.write("Welcome to my AI-enhanced interactive portfolio!")

# ----- Projects -----
st.markdown("## 🚀 Projects")

project_list = {
    "SecureTrack 🔒": "Cybersecurity automation using Python and log monitoring.",
    "SalesViz 360 📊": "Power BI dashboard for sales insights.",
    "AutoMail Pro 📧": "Automated bulk mailer using Python.",
    "AI Portfolio 🤖": "This futuristic portfolio site built using Streamlit.",
}

for title, desc in project_list.items():
    st.markdown(f"### {title}")
    st.write(desc)

# ----- Footer -----
st.markdown("---")
st.write("📫 Reach me at: vishnudumpala@email.com | [GitHub](https://github.com/vishnuvardhan) | [LinkedIn](https://linkedin.com)")

