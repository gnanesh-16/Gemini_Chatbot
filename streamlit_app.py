# import streamlit as st
# import os
# import google.generativeai as genai

# # Initialize Gemini-Pro 
# genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
# model = genai.GenerativeModel('gemini-pro')

# def role_to_streamlit(role):
#   if role == "model":
#     return "assistant"
#   else:
#     return role

# # Add a Gemini Chat history object to Streamlit session state
# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history = [])

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
#     with st.chat_message("assistant"):
#         st.markdown(response.text)

import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Function to convert chat history to text
def convert_chat_to_text(chat_history):
    text = ""
    for message in chat_history:
        text += f"{role_to_streamlit(message.role)}: {message.parts[0].text}\n"
    return text

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("Chat with Google Gemini-Pro!")

# Display chat messages from history above the current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)

    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)

# Add a button to download the chat history as a text file
if st.button("Download Chat History"):
    chat_text = convert_chat_to_text(st.session_state.chat.history)
    st.download_button(
        label="Download Chat",
        data=chat_text,
        file_name="chat_history.txt",
        key="download_button"
    )
