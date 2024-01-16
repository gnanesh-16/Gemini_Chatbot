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
import os
import google.generativeai as genai
from PIL import Image
import fitz  # PyMuPDF

# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display Form Title
st.title("Chat with Google Gemini-Pro!")

# Display chat messages from history above the current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept the user's next message, add to context, resubmit the context to Gemini
if prompt := st.text_input("I possess a well of knowledge. What would you like to know?"):
    # Display the user's last message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Send the user's entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display the last 
    with st.chat_message("assistant"):
        st.markdown(response.text)

# Image uploading
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    # If users ask about the image, provide a response
    if "IMAGE" in prompt.upper():
        with st.chat_message("assistant"):
            st.write("You asked about the uploaded image. Provide a relevant response.")  # Modify as needed

# PDF uploading
uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_pdf is not None:
    pdf_content = uploaded_pdf.read()
    
    # Convert PDF to vectors using PyMuPDF
    doc = fitz.open("pdf", pdf_content)

    # Extract text from each page
    text_content = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text_content += page.get_text()

    # Simple bag-of-words vectorization (you may replace with your vectorization logic)
    pdf_vectors = text_content.split()

    # If users ask about PDF, display the vectors or any specific information
    if "PDF" in prompt.upper():
        with st.chat_message("assistant"):
            st.write("PDF Vectors:", pdf_vectors)  # Display vectors or modify as needed
