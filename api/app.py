import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain Server", version="1.0", description="A simple API Server"
)

# Initialize the Ollama model with llama2
llm = Ollama(model="llama2")

# Define the prompts
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 years child with 100 words"
)

# Add routes for the prompts using the Ollama model
add_routes(app, prompt1 | llm, path="/essay")

add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
