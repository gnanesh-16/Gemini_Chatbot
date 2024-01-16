# import os
# import textwrap
# import streamlit as st
# import google.generativeai as genai


# genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
# model = genai.GenerativeModel('gemini-pro')

# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history=[])

# if (prompt := st.text_input("What can I do for you?")):
    
#     response = st.session_state.chat.send_message(prompt)

#     response_markdown = textwrap.dedent(response.text).strip()
#     with st.chat_message("assistant"):
#         st.markdown(response_markdown, unsafe_allow_html=True)

# if "chat" in st.session_state:
#     for message in st.session_state.chat.history:
#         with st.chat_message("user" if message.role == "user" else "assistant"):
#             st.markdown(textwrap.dedent(message.parts[0].text).strip(), unsafe_allow_html=True)

import os
import textwrap
import streamlit as st
import google.generativeai as genai

# Add your Gemini API key here
genai.configure(api_key="GOOGLE_GEMINI_API_KEY")

model = genai.GenerativeModel('gemini-pro')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Left side menu
st.sidebar.header("Image and Query")

# Image uploading button
uploaded_image = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Additional input box for queries related to the image
image_query = st.sidebar.text_input("Image Query", "")

# Submit button
if st.sidebar.button("Submit"):
    if uploaded_image:
        # Perform image-related tasks here using the uploaded_image variable
        st.sidebar.success("Image Uploaded Successfully!")
        
        # You can use the image_query variable to generate a response
        if image_query:
            response = st.session_state.chat.send_message(image_query)
            
            response_markdown = textwrap.dedent(response.text).strip()
            with st.chat_message("assistant"):
                st.markdown(response_markdown, unsafe_allow_html=True)
    else:
        st.sidebar.warning("Please upload an image first.")

# Main content area
if (prompt := st.text_input("What can I do for you?")):
    response = st.session_state.chat.send_message(prompt)
    
    response_markdown = textwrap.dedent(response.text).strip()
    with st.chat_message("assistant"):
        st.markdown(response_markdown, unsafe_allow_html=True)

if "chat" in st.session_state:
    for message in st.session_state.chat.history:
        with st.chat_message("user" if message.role == "user" else "assistant"):
            st.markdown(textwrap.dedent(message.parts[0].text).strip(), unsafe_allow_html=True)





