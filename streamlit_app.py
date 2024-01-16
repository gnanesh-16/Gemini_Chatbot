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
    st.session_state.chat = model.start_chat(history = [])

# Display Form Title
st.title("Chat with Google Gemini-Pro!")

# Create a sidebar for image upload and query submission
with st.sidebar:
    # Display instructions for image upload
    st.markdown("**Image Upload:**")
    st.markdown("Upload an image to ask questions about.")

    # Add a file uploader for the image
    uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    # Add a submit button to submit the image for analysis
    submit_button = st.button("Submit Image")

    # Add an input box for the user to ask queries about the image
    query_input = st.text_input("Ask a question about the image:")

# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Check if the user has uploaded an image
if uploaded_image is not None:
    # Check if the user has submitted the image
    if submit_button:
        # Send the image to Gemini for analysis
        response = model.analyze_image(uploaded_image.getvalue())

        # Display the results of the image analysis
        with st.chat_message("assistant"):
            st.image(uploaded_image, caption="Uploaded Image")
            st.markdown(response.description)

# Check if the user has asked a query about the image
if query_input:
    # Send the query to Gemini
    response = st.session_state.chat.send_message(query_input)

    # Display the response to the query
    with st.chat_message("assistant"):
        st.markdown(response.text)
