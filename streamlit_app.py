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

# # Add your Gemini API key here
# genai.configure(api_key="GOOGLE_GEMINI_API_KEY")

# model = genai.GenerativeModel('gemini-pro')

# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history=[])

# # Left side menu
# st.sidebar.header("Image and Query")

# # Image uploading button
# uploaded_image = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# # Additional input box for queries related to the image
# image_query = st.sidebar.text_input("Image Query", "")

# # Submit button
# if st.sidebar.button("Submit"):
#     if uploaded_image:
#         # Perform image-related tasks here using the uploaded_image variable
#         st.sidebar.success("Image Uploaded Successfully!")
        
#         # You can use the image_query variable to generate a response
#         if image_query:
#             response = st.session_state.chat.send_message(image_query)
            
#             response_markdown = textwrap.dedent(response.text).strip()
#             with st.chat_message("assistant"):
#                 st.markdown(response_markdown, unsafe_allow_html=True)
#     else:
#         st.sidebar.warning("Please upload an image first.")

# # Main content area
# if (prompt := st.text_input("What can I do for you?")):
#     response = st.session_state.chat.send_message(prompt)
    
#     response_markdown = textwrap.dedent(response.text).strip()
#     with st.chat_message("assistant"):
#         st.markdown(response_markdown, unsafe_allow_html=True)

# if "chat" in st.session_state:
#     for message in st.session_state.chat.history:
#         with st.chat_message("user" if message.role == "user" else "assistant"):
#             st.markdown(textwrap.dedent(message.parts[0].text).strip(), unsafe_allow_html=True)



from dotenv import load_dotenv
load_dotenv() 
import streamlit as st
import os
from PIL import Image
import textwrap
import google.generativeai as genai

# Configure Gemini AI API key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))

# Load Gemini pro vision model
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, user_prompt):
    response = model.generate_content([input, image[0], user_prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Left side menu for chatting with Gemini AI
st.sidebar.header("Gemini AI Chat")
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Chat input box
if (prompt := st.sidebar.text_input("Chat with Gemini AI")):
    response = st.session_state.chat.send_message(prompt)
    response_markdown = textwrap.dedent(response.text).strip()
    with st.sidebar.chat_message("assistant"):
        st.sidebar.markdown(response_markdown, unsafe_allow_html=True)

# Main content area for MultiLanguage Invoice Extractor
st.title("MultiLanguage Invoice Extractor")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice,
and you will have to answer any questions based on the uploaded invoice image 
and also provide it in table formate of invoice details.
"""

st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

# If submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, prompt)
    st.subheader("The Response is")
    st.write(response)



