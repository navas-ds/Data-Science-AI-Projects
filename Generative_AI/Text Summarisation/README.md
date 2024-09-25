# Text Summarisation from YT and Website

This project is a Streamlit web application that summarizes content from YouTube videos or websites using Langchain, Groq API, and large language models. It provides an easy way to get concise summaries of long-form content directly from URLs.

## Features

- Summarize content from YouTube videos and websites.
- Uses the Groq API and Langchain's `Gemma-7b-It` model for generating summaries.
- Simple and user-friendly Streamlit interface.

## Requirements

- Python 3.10 or later
- Groq API Key
- Libraries: `validators`, `streamlit`, `langchain`, `langchain_groq`, `langchain_community`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/navas-ds/Data-Science-AI-Projects/tree/main/Generative_AI/Text%20Summarisation.git
    cd Text Summarisation
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Enter your Groq API key in the sidebar and the URL of the content you wish to summarize. Click the **"Summarize the content from YT or Website"** button to get a summary.

## Project Structure

- `app.py`: Main file containing the Streamlit app code.
- `requirements.txt`: Lists all the dependencies needed to run the project.

## Technologies Used

- **Langchain**: For handling the summarization process using language models.
- **Groq API**: To access and run the Gemma model.
- **Streamlit**: For building the user interface.
- **YouTube and Website Loaders**: To fetch content from specified URLs.

## Contributing

Contributions are welcome! If you have ideas for improvements, feel free to fork the project and submit a pull request.


## Acknowledgments

- [Langchain](https://github.com/langchain-ai/langchain) - Framework for building applications with language models.
- [Streamlit](https://streamlit.io/) - Open-source app framework for Machine Learning and Data Science projects.
- [Groq](https://groq.com/) - For providing the Groq API and model access.

