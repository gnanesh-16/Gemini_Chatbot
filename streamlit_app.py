# import streamlit as st
# import os
# import google.generativeai as genai

# # Initialize Gemini-Pro 
# genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
# model = genai.GenerativeModel('gemini-pro')

# # Gemini uses 'model' for assistant; Streamlit uses 'assistant'
# def role_to_streamlit(role):
#   if role == "model":
#     return "assistant"
#   else:
#     return role

# # Add a Gemini Chat history object to Streamlit session state
# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history = [])

# # Display Form Title
# st.title("Chat with Google Gemini-Pro!")

# # Display chat messages from history above current input box
# for message in st.session_state.chat.history:
#     with st.chat_message(role_to_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# # Accept user's next message, add to context, resubmit context to Gemini
# if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
#     # Display user's last message
#     st.chat_message("user").markdown(prompt)
    
#     # Send user entry to Gemini and read the response
#     response = st.session_state.chat.send_message(prompt) 
    
#     # Display last 
#     with st.chat_message("assistant"):
#         st.markdown(response.text)


import streamlit as st
import mysql.connector
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Create a function to handle the login process
def login(username, password):
    # Connect to the SQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database_name"
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the SQL query to check if the user exists
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    # Fetch the results
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Return True if the user exists, False otherwise
    return len(results) > 0

# Create a connection to the SQL database
connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)

# Create a cursor object
cursor = connection.cursor()

# Add a login form to the Streamlit app
st.header("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
submitted = st.button("Login")

# Check if the user has submitted the login form
if submitted:
    # Call the login function to check if the login was successful
    login_successful = login(username, password)

    # Store the user's information in a session state variable
    if login_successful:
        st.session_state.logged_in = True
        st.session_state.username = username

# Use the session state variable to control access to the chatbot
if st.session_state.logged_in:
    # Display a welcome message to the user
    st.write(f"Welcome, {st.session_state.username}!")

    # Add a Gemini Chat history object to Streamlit session state
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history = [])

    # Display Form Title
    st.title("Chat with Google Gemini-Pro!")

    # Display chat messages from history above current input box
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Accept user's next message, add to context, resubmit context to Gemini
    if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
        # Display user's last message
        st.chat_message("user").markdown(prompt)

        # Send user entry to Gemini and read the response
        response = st.session_state.chat.send_message(prompt) 

        # Display last 
        with st.chat_message("assistant"):
            st.markdown(response.text)

else:
    # Display a message to users who are not logged in
    st.write("Please login to access the chatbot.")

# Close the cursor and connection
cursor.close()
connection.close()
