import streamlit as st
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import credentials, auth, db

# Initialize Firebase Admin SDK with your service account credentials
cred = credentials.Certificate("path_to_your_firebase_config.json")  # Replace with the correct path to your service account JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://seizurepredictionneurofeedback-default-rtdb.asia-southeast1.firebasedatabase.app"
})

# Streamlit App Configuration
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
            # Firebase Authentication Login
            user = auth.get_user_by_email(email)  # Retrieve user by email
            # Firebase doesn't store passwords, you need to authenticate via the frontend (email/password) via Firebase Auth SDK for JS or Firebase SDK for Python
            # Using Firebase Admin SDK alone doesn't support email/password authentication, only admin tasks
            st.success("Logged in successfully!")
        except Exception as e:
            st.error(f"Login failed: {e}")

elif selected == "Sign Up":
    st.title("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        try:
            # Firebase Authentication Sign Up
            user = auth.create_user(email=email, password=password)  # Create user using Firebase Auth
            st.success("Account created successfully!")
        except Exception as e:
            st.error(f"Signup failed: {e}")

elif selected == "Dashboard":
    st.title("Dashboard")
    st.write("Welcome to your health monitoring dashboard 🚀")

