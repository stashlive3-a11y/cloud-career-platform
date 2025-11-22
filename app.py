import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Cloud Career", page_icon="☁️", layout="wide")

# Simple app
st.title("☁️ Cloud Career Management Platform")
st.markdown("---")

# Check if user is logged in
if not st.session_state.get('logged_in'):
    # Show login/register
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.user = {"name": email.split('@')[0]}
                st.success("Login successful! 🎉")
                st.rerun()
            else:
                st.warning("Please enter email and password")
    
    with tab2:
        new_email = st.text_input("New Email")
        new_name = st.text_input("Full Name")
        if st.button("Create Account"):
            if new_email and new_name:
                st.success("Account created! Please login.")
            else:
                st.warning("Please fill all fields")
            
else:
    # User is logged in - show main app
    st.sidebar.success(f"Welcome, {st.session_state.user['name']}! 👋")
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    # Navigation
    page = st.sidebar.selectbox("Menu", ["Dashboard", "Profile", "Find Mentors", "Learning Paths"])
    
    if page == "Dashboard":
        st.header("📊 Dashboard")
        st.write("Welcome to your Cloud Career Dashboard!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Cloud Skills", "5", "+2")
        with col2:
            st.metric("Mentor Sessions", "2", "+1")
        with col3:
            st.metric("Certifications", "1", "0")
            
    elif page == "Profile":
        st.header("👤 Your Profile")
        name = st.text_input("Full Name", value=st.session_state.user['name'])
        email = st.text_input("Email")
        role = st.selectbox("Current Role", ["Cloud Engineer", "DevOps", "Solutions Architect", "Student", "IT Professional"])
        
        if st.button("Save Profile"):
            st.session_state.user['name'] = name
            st.success("Profile saved successfully! ✅")
        
    elif page == "Find Mentors":
        st.header("👥 Find Cloud Mentors")
        
        mentors = [
            {"name": "John AWS Expert", "skills": "AWS, DevOps", "experience": "8 years", "rating": "⭐️⭐️⭐️⭐️⭐️"},
            {"name": "Sarah Azure Pro", "skills": "Azure, Security", "experience": "6 years", "rating": "⭐️⭐️⭐️⭐️"},
            {"name": "Mike GCP Specialist", "skills": "GCP, Kubernetes", "experience": "7 years", "rating": "⭐️⭐️⭐️⭐️⭐️"}
        ]
        
        for mentor in mentors:
            st.subheader(mentor['name'])
            st.write(f"**Skills:** {mentor['skills']}")
            st.write(f"**Experience:** {mentor['experience']}")
            st.write(f"**Rating:** {mentor['rating']}")
            if st.button(f"Book Session with {mentor['name'].split()[0]}", key=mentor['name']):
                st.success(f"Session request sent to {mentor['name']}! 📅")
            st.markdown("---")
            
    elif page == "Learning Paths":
        st.header("📚 Cloud Learning Paths")
        
        paths = [
            {"name": "AWS Solutions Architect", "level": "Beginner", "duration": "40 hours"},
            {"name": "Azure Administrator", "level": "Intermediate", "duration": "35 hours"},
            {"name": "GCP Cloud Engineer", "level": "Beginner", "duration": "30 hours"}
        ]
        
        for path in paths:
            st.subheader(path['name'])
            st.write(f"**Level:** {path['level']}")
            st.write(f"**Duration:** {path['duration']}")
            if st.button(f"Start {path['name']}", key=path['name']):
                st.success(f"Enrolled in {path['name']}! 🚀")
            st.markdown("---")
