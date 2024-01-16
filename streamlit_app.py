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
import FPDF
import google.generativeai as genai
from fpdf import FPDF  # Import FPDF library for creating PDF

# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Function to convert chat history to PDF
def save_chat_to_pdf(chat_history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for message in chat_history:
        pdf.cell(200, 10, txt=message.parts[0].text, ln=True)
    pdf_output = "chat_history.pdf"
    pdf.output(pdf_output)
    return pdf_output

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

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
    with st.chat_message("assistant"):
        st.markdown(response.text)

# Add a download button for the chat conversation as a PDF
if st.button("Download Chat as PDF"):
    pdf_file = save_chat_to_pdf(st.session_state.chat.history)
    st.markdown(f"Download your chat as [PDF](sandbox:/path/to/{pdf_file})")
