# Langchain-SearchBot With Tools And Agent
This project is a Streamlit web application that integrates Langchain with Groq's language model, allowing you to create a chatbot that can search the web and answer queries using Wikipedia, Arxiv, and DuckDuckGo. The application leverages Langchain's agents and Streamlit to provide an interactive interface where users can chat with the AI, ask questions, and receive real-time answers from various sources.

## Features
- Web Search: Uses DuckDuckGo for general web searches.
- Arxiv Search: Queries research papers from Arxiv with concise results.
- Wikipedia Search: Fetches summarized information from Wikipedia.
- Interactive Interface: Real-time chat interaction using Streamlit.
- Callback Handler: Displays the agent's reasoning steps directly in the Streamlit interface.

## Prerequisites
- Python 3.10
- Streamlit
- Langchain
- Groq API Key

## Usage
- Enter your Groq API key in the settings sidebar.
- Type a question or prompt in the chat box, and the chatbot will respond using its search capabilities.
- Watch the agent’s thoughts and actions update live as it processes your query.

