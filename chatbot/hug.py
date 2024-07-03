
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic you want")

# Load LLAMA2 model and tokenizer from Hugging Face with authentication
model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=os.environ["HUGGINGFACE_API_KEY"])
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=os.environ["HUGGINGFACE_API_KEY"])

# Create a Hugging Face pipeline
hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=100
)

# Integrate Hugging Face pipeline with Langchain
llm = HuggingFacePipeline(pipeline=hf_pipeline)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Handling user input and displaying output
if input_text:
    st.write(chain.invoke({"question": input_text}))
