from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

def generate_response_with_groq(history, question, model_name):
    # Add the new question to the chat history
    history.append(("user", question))

    # Create prompt with entire chat history
    prompt = ChatPromptTemplate.from_messages(history)

    # Initialize Groq API model
    model = ChatGroq(model=model_name, api_key=groq_api_key)
    output_parser = StrOutputParser()

    # Create the chain
    chain = prompt | model | output_parser

    # Prepare the input for the model
    formatted_input = {'text': question}

    # Pass the input to the Groq's API for fast inference
    response = chain.invoke(formatted_input)

    # Add the model's response to the history
    history.append(("assistant", response))

    return response

# Dropdown to select various models supported by Groq
model_name = st.sidebar.selectbox('Select a Groq model', ["Gemma2-9b-It", "Gemma-7b-It", "llama3-8b-8192","llama3-70b-8192"])

# Main Interface for User input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response_with_groq(st.session_state.history, user_input, model_name)

    # Display conversation history
    for message in st.session_state.history:
        role, content = message
        if role == "user":
            st.write(f"**You:** {content}")
        else:
            st.write(f"**Assistant:** {content}")
else:
    st.write("Please provide a query")
