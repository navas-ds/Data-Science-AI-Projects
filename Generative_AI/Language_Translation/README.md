# Simple Language Translation

This project sets up a FastAPI server that integrates with Langchain for translation tasks. It uses the `ChatGroq` model to translate text based on user input. The server provides a simple API endpoint to handle translation requests.

## Features

- **FastAPI Server**: A lightweight web framework for building APIs.
- **Langchain Integration**: Uses the `ChatGroq` model for handling translation tasks.
- **Environment Variable Management**: Loads sensitive information like API keys from a `.env` file.
- **Dynamic Prompting**: Allows dynamic language translation based on user input.

## Requirements

- Python 3.10 or higher
- FastAPI
- Uvicorn
- Langchain
- Langserve
- Dotenv
- Additional dependencies listed in `requirements.txt`


