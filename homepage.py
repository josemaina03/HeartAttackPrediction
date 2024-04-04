import streamlit as st
import mysql.connector
from mysql.connector import connect
from streamlit_extras.switch_page_button import switch_page

# Define a session state to keep track of the current page
class SessionState:
    def __init__(self):
        self.current_page = "login"

# Create an instance of the session state
session_state = SessionState()

# Function to connect to MySQL database
def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="streamlit_login"
    )
    return conn

# Function to authenticate user
def authenticate_user(username, password):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    else:
        return False

# Function to sign up new user
def sign_up_user(username, password):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    else:
        return False

# Function to reset user's password
def reset_password(username, new_password):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE users SET password = %s WHERE username = %s"
        cursor.execute(query, (new_password, username))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    else:
        return False

# Streamlit login page
def main():
    st.title("Login Page")
    username_login = st.text_input("Login Username")
    password_login = st.text_input("Login Password", type="password")
    if st.button("Login"):
        if authenticate_user(username_login, password_login):
            session_state.current_page = 'heart_attack'
            switch_page(session_state.current_page)
            # Redirect to dashboard or desired page after successful login
        else:
            st.error("Invalid username or password")

    st.title("Sign Up")
    with st.expander("New User? Sign Up Here"):
        username_signup = st.text_input("Sign Up Username")
        password_signup = st.text_input("Sign Up Password", type="password")
        if st.button("Sign Up"):
            if sign_up_user(username_signup, password_signup):
                st.success('User created successfully')
            else:
                st.error("Sign up failed. Please try again.")
    
    # Forgot Password
    st.title("Forgot Password")
    with st.expander("Forgot your password?"):
        username_forgot = st.text_input("Enter your username")
        new_password = st.text_input("Enter your new password", type="password")
        if st.button("Reset Password"):
            if reset_password(username_forgot, new_password):
                st.success("Password reset successfully")
            else:
                st.error("Failed to reset password. Please try again.")

    

if __name__ == "__main__":
    main()
