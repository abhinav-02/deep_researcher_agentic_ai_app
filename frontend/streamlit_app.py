import streamlit as st
import requests

st.title("Deep Research Agent")

topic = st.text_input(
    "Research Topic"
)

if st.button("Research"):

    response = requests.post(
    "http://127.0.0.1:8000/research",
    json={"query": topic},
    timeout=300
)
    

    result = response.json()

    st.subheader("Research Plan")

    st.write(result["plan"])