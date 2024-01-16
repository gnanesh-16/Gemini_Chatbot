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
    st.session_state.chat = model.start_chat(history=[])

# Display Form Title
st.title("Chat with Google Gemini-Pro!")

# Cool-looking dropdown menu for selecting assistant personalities/modes
st.markdown("<h2 style='text-align: center; color: #1E88E5;'>Select Assistant Mode</h2>", unsafe_allow_html=True)
personalities = ["Friendly", "Professional", "Funny", "Serious"]
personality_option = st.selectbox("Choose Assistant Mode", personalities)

# Button to change assistant's personality
if st.button("Change Personality"):
    # Set the assistant's personality based on the user's selection
    if personality_option == "Friendly":
        st.session_state.chat = model.start_chat(history=[], personality="friendly")
    elif personality_option == "Professional":
        st.session_state.chat = model.start_chat(history=[], personality="professional")
    elif personality_option == "Funny":
        st.session_state.chat = model.start_chat(history=[], personality="funny")
    elif personality_option == "Serious":
        st.session_state.chat = model.start_chat(history=[], personality="serious")

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

