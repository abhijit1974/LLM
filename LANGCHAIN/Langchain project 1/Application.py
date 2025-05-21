import streamlit as st
import requests
import json

import os
from dotenv import load_dotenv
load_dotenv()

## LangSmith Tracking, You will need to build a separate .env file and store your API key there
## and then load it using the load_dotenv() function.

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

from langchain_ollama.llms import OllamaLLM

st.title("Simple Question Answering with Ollama")

user_question = st.text_input("Ask your question:")

def query_ollama(prompt, model="llama3.2:latest"):
    """Sends a prompt to the Ollama API and returns the response."""
  
    data = {
        "prompt": prompt,
        "model": model,
        "stream": False  # For a single response
    }
    try:
        response = requests.post(url, json=data, stream=False)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"
    except json.JSONDecodeError:
        return "Error decoding Ollama response."




if user_question:
    with st.spinner("Thinking..."):
        answer = query_ollama(user_question)
    st.subheader("Answer:")
    st.write(answer)