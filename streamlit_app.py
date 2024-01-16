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

# import os
# import textwrap
# import streamlit as st
# import google.generativeai as genai

# # Configure generative AI
# genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
# model = genai.GenerativeModel('gemini-pro')

# # Initialize or retrieve chat session
# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history=[])
# else:
#     # Retrieve chat history and restart the chat
#     chat_history = st.session_state.chat.history
#     st.session_state.chat = model.start_chat(history=chat_history)

# # User input and bot response
# prompt = st.text_input("Ask me a question")

# if prompt:
#     # Send user input to the chat model
#     response = st.session_state.chat.send_message(prompt)

#     # Display bot response
#     response_markdown = textwrap.dedent(response.text).strip()
#     with st.chat_message("assistant"):
#         st.markdown(response_markdown, unsafe_allow_html=True)

# # Display chat history
# if "chat" in st.session_state:
#     for message in st.session_state.chat.history:
#         with st.chat_message("user" if message.role == "user" else "assistant"):
#             st.markdown(textwrap.dedent(message.parts[0].text).strip(), unsafe_allow_html=True)

import os
import io
import textwrap
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure generative AI
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Initialize or retrieve chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display chat history on the left side
st.sidebar.header("Chat History")
for message in st.session_state.chat.history:
    st.sidebar.markdown(
        textwrap.dedent(message.parts[0].text).strip(),
        unsafe_allow_html=True
    )

# User input for text and photo
prompt = st.text_area("Type your message", key="user_input")
uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

if st.button("Send"):
    if prompt:
        # Send user text input to the chat model
        response = st.session_state.chat.send_message(prompt)

        # Display bot response
        response_markdown = textwrap.dedent(response.text).strip()
        with st.chat_message("assistant"):
            st.markdown(response_markdown, unsafe_allow_html=True)

    if uploaded_file:
        # Process the uploaded image
        image = Image.open(uploaded_file)
        
        # Convert image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_data = image_bytes.getvalue()

        # Use the generative AI API to get a response based on the image
        image_response = genai.image_to_text(image_data)
        
        # Display the response
        with st.chat_message("assistant"):
            st.write("Response from image:", image_response)

# Display chat history (main chat area)
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(textwrap.dedent(message.parts[0].text).strip(), unsafe_allow_html=True)



