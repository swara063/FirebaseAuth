import streamlit as st
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import credentials, auth, db
import os
import tempfile

# Prompt user to upload Firebase service account credentials JSON file
st.title("Firebase Authentication App")

uploaded_file = st.file_uploader("Upload your Firebase credentials JSON file", type=["json"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    try:
        # Check if Firebase has already been initialized
        if not firebase_admin._apps:
            # Initialize Firebase Admin SDK with the uploaded service account credentials
            cred = credentials.Certificate(tmp_file_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': "https://seizurepredictionneurofeedback-default-rtdb.asia-southeast1.firebasedatabase.app"
            })

        # Firebase Authentication actions
        selected = option_menu(
            menu_title=None,
            options=["Login", "Sign Up", "Dashboard"],
            icons=["box-arrow-in-right", "person-plus", "speedometer"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )

        if selected == "Login":
            st.title("Login")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                try:
                    # Login using Firebase Authentication
                    user = auth.get_user_by_email(email)  # Retrieve user by email
                    st.success("Logged in successfully!")
                except Exception as e:
                    st.error(f"Login failed: {e}")

        elif selected == "Sign Up":
            st.title("Sign Up")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Sign Up"):
                try:
                    # Sign Up using Firebase Authentication
                    user = auth.create_user(email=email, password=password)  # Create user
                    st.success("Account created successfully!")
                except Exception as e:
                    st.error(f"Signup failed: {e}")

        elif selected == "Dashboard":
            st.title("Dashboard")
            st.write("Welcome to your health monitoring dashboard 🚀")
    except Exception as e:
        st.error(f"Error initializing Firebase: {e}")


