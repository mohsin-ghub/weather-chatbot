import streamlit as st
from openrouter_utils import extract_city
from weather_api import get_weather

st.set_page_config(page_title="Smart Weather Chatbot", page_icon="⛅")

st.title("🌤️ Smart Weather Chatbot with OpenRouter")
st.write("Ask me about the weather in any city!")

user_input = st.text_input("Type your query (e.g., What's the weather in Mumbai?)")

if st.button("Get Weather"):
    if user_input:
        city = extract_city(user_input)
        st.write(f"🗺️ Detected City: **{city}**")

        weather_info = get_weather(city)
        st.success(weather_info)
    else:
        st.warning("Please enter a query!")

st.markdown("---")
st.caption("🔹 Powered by OpenRouter + DeepSeek & OpenWeather | Built with Streamlit")
