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
import google.generativeai as genai 
import google.ai.generativelanguage as glm 
from dotenv import load_dotenv
from PIL import Image
import os 
import io 

load_dotenv()

def image_to_byte_array(image: Image) -> bytes:
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr=imgByteArr.getvalue()
    return imgByteArr

API_KEY = os.environ.get("GOOGLE_GEMINI_KEY")
genai.configure(api_key=API_KEY)

st.image("./Google-Gemini-AI-Logo.png", width=200)
st.write("")

gemini_pro, gemini_vision = st.tabs(["Gemini Pro", "Gemini Pro Vision"])

def main():
    with gemini_pro:
        st.header("Interact with Gemini Pro")
        st.write("")

        prompt = st.text_input("prompt please...", placeholder="Prompt", label_visibility="visible")
        model = genai.GenerativeModel("gemini-pro")

        if st.button("SEND",use_container_width=True):
            response = model.generate_content(prompt)

            st.write("")
            st.header(":blue[Response]")
            st.write("")

            st.markdown(response.text)

    with gemini_vision:
        st.header("Interact with Gemini Pro Vision")
        st.write("")

        image_prompt = st.text_input("Interact with the Image", placeholder="Prompt", label_visibility="visible")
        uploaded_file = st.file_uploader("Choose and Image", accept_multiple_files=False, type=["png", "jpg", "jpeg", "img", "webp"])

        if uploaded_file is not None:
            st.image(Image.open(uploaded_file), use_column_width=True)

            st.markdown("""
                <style>
                        img {
                            border-radius: 10px;
                        }
                </style>
                """, unsafe_allow_html=True)
            
        if st.button("GET RESPONSE", use_container_width=True):
            model = genai.GenerativeModel("gemini-pro-vision")

            if uploaded_file is not None:
                if image_prompt != "":
                    image = Image.open(uploaded_file)

                    response = model.generate_content(
                        glm.Content(
                            parts = [
                                glm.Part(text=image_prompt),
                                glm.Part(
                                    inline_data=glm.Blob(
                                        mime_type="image/jpeg",
                                        data=image_to_byte_array(image)
                                    )
                                )
                            ]
                        )
                    )

                    response.resolve()

                    st.write("")
                    st.write(":blue[Response]")
                    st.write("")

                    st.markdown(response.text)

                else:
                    st.write("")
                    st.header(":red[Please Provide a prompt]")

            else:
                st.write("")
                st.header(":red[Please Provide an image]")

if __name__ == "__main__":
    main()
