import os

import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}"),
    ]
)

# Streamlit framework
st.title("Langchain Demo With LLAMA2 API")
input_text = st.text_input("Search the topic you want")

# Ollama LLama2 LLM
try:
    llm = Ollama(model="llama2")  # pylint: disable=not-callable
except TypeError as e:
    st.error(f"Error initializing Ollama: {e}")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        response = chain.invoke({"question": input_text})
        st.write(response)
    except Exception as e:
        st.error(f"Error during chain invocation: {e}")
