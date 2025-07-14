import streamlit as st
from gemini_utils import extract_city

st.title("🌤️ Smart Weather Chatbot — NLP Test")

user_input = st.text_input("Ask about the weather:")

if st.button("Extract City"):
    city = extract_city(user_input)
    st.write(f"🗺️ Detected City: {city}")
