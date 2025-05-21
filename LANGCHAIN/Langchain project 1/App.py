
#Basic Application using Langchain and Ollama LLM


import os
from dotenv import load_dotenv

from langchain_ollama.llms import OllamaLLM

##rom langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## LangSmith Tracking, You will need to build a separate .env file and store your API key there
## and then load it using the load_dotenv() function.

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a expert created by Abhijit Das. Please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

## Streamlit Framework

st.title("Abhijit's Langchain Demo with llama3.2:latest")
input_text=st.text_input("what question do you have in mind?")

## Ollama Model Llama3.2

llm=OllamaLLM(model="llama3.2:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    with st.spinner("Thinking..."):
        st.write(chain.invoke({"question": input_text}))
     

## Run the app using the command from command prompt in appropriate location >streamlit run app.py
