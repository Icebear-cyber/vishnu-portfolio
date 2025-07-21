import streamlit as st

st.title("💼 Projects")

st.write("""
Here are some of the best projects I've worked on. Each one showcases unique skills in Python, automation, and problem-solving.
""")

# Project 1
st.subheader("📧 AutoMail Pro – Smart Email Automation")
st.write("""
An advanced Python script to send personalized, scheduled, and bulk emails with attachments using SMTP and Excel integration.

**Tech:** Python, `smtplib`, `openpyxl`, `schedule`
""")
st.link_button("🔗 View on GitHub", "https://github.com/yourusername/automail-pro")

# Project 2
st.subheader("🔐 SecureTrack – Cybersecurity Automation Tool")
st.write("""
A tool to scan log files and detect suspicious activity using regex and automation, with optional threat classification using machine learning.

**Tech:** Python, Regex, `pandas`, Scikit-learn
""")
st.link_button("🔗 View on GitHub", "https://github.com/yourusername/securetrack")

# Project 3
st.subheader("📊 SalesViz 360 – Power BI Sales Dashboard")
st.write("""
A complete dashboard solution to visualize and analyze sales data, customer trends, and product performance.

**Tech:** Power BI, DAX, Excel
""")
st.link_button("🔗 View on GitHub", "https://github.com/yourusername/salesviz-360")
