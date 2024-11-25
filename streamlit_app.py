import streamlit as st
import google.generativeai as genai

# Tạo header
st.header('CONGSANMUONNAM🤖')
st.markdown("I am HO CHI MINH Chatbot based on Genimi-Pro what can I help you today 😊")
with st.sidebar:
    API_input = st.text_input("Gemini API Key" , type="password")

try:
    genai.configure(api_key= API_input)

    user_input = st.text_input("Type your question here and press Enter" , key="user_input")

    model = genai.GenerativeModel('gemini-pro')

    if user_input:
        if not API_input:
            st.warning("Please enter your [API](https://ai.google.dev/) into sidebar.")
        else:
            response = model.generate_content(user_input)
            for letters in respone.text:
                st.write(letters)
        
except Exception:
    st.error('Please enter the correct [API](https://ai.google.dev/) Key')
