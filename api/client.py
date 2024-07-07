import requests
import streamlit as st


def get_essay_response(topic):
    response = requests.post(
        "http://localhost:8000/essay/invoke", json={"input": {"topic": topic}}
    )
    return response.json()["output"]


def get_poem_response(topic):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": topic}}
    )
    return response.json()["output"]


# Streamlit framework
st.title("Langchain Demo with LLAMA2 API")

# Inputs for essay and poem topics
essay_topic = st.text_input("Write an essay on")
poem_topic = st.text_input("Write a poem on")

# Display the responses
if essay_topic:
    st.write(get_essay_response(essay_topic))

if poem_topic:
    st.write(get_poem_response(poem_topic))
