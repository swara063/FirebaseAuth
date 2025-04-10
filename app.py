import streamlit as st
from streamlit_option_menu import option_menu
import pyrebase

# Firebase config
firebaseConfig = {
    "apiKey": "AIzaSyDBNGuUhj6vBp5ZIGQGrM1xQomYtSYKAyQ",
    "authDomain": "seizurepredictionneurofeedback.firebaseapp.com",
    "databaseURL": "https://seizurepredictionneurofeedback-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "seizurepredictionneurofeedback",
    "storageBucket": "seizurepredictionneurofeedback.firebasestorage.app",
    "messagingSenderId": "575405480415",
    "appId": "1:575405480415:web:4aaf89ef37ecfea510cc6a"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Streamlit App
st.set_page_config(page_title="Seizure Prediction App", page_icon="🧠", layout="wide")

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Login", "Sign Up", "Dashboard"],
    icons=["box-arrow-in-right", "person-plus", "speedometer"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Screens
if selected == "Login":
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Logged in successfully!")
        except Exception as e:
            st.error(f"Login failed: {e}")

elif selected == "Sign Up":
    st.title("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Account created successfully!")
        except Exception as e:
            st.error(f"Signup failed: {e}")

elif selected == "Dashboard":
    st.title("Dashboard")
    st.write("Welcome to your health monitoring dashboard 🚀")
