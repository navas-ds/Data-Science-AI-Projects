# YouTube Blog Content Generation

This project utilizes the **Crew AI** framework, along with the **Ollama** model and **YouTube API**, to create a blog content generation system. It leverages video transcriptions from a specific YouTube channel and narrates engaging tech stories.

## Overview

The application consists of two primary agents:
1. **Blog Researcher**: Fetches relevant video transcriptions from the provided YouTube channel.
2. **Blog Writer**: Creates compelling narratives based on the research conducted by the Blog Researcher.

## Project Structure

The project includes the following files:

- **`agents.py`**: Defines the Blog Researcher and Blog Writer agents.
- **`crew.py`**: Initializes the crew, orchestrating the tasks assigned to agents.
- **`tasks.py`**: Contains definitions for the research and writing tasks.
- **`tools.py`**: Configures tools like the YouTube Channel Search Tool used for fetching video data.
- **`requirements.txt`**: Dependencies

## File Descriptions
### agents.py
Defines two agents:

#### Blog Researcher: Responsible for fetching video transcriptions.
#### Blog Writer: Crafts engaging narratives from the fetched information.
### crew.py
Forms the crew with defined agents and tasks. It manages the workflow and starts the task execution.

### tasks.py
Defines the tasks to be performed by the agents:

#### Research Task: Gathers video information based on the provided topic.
#### Writing Task: Summarizes the gathered information into a blog format.

### tools.py
Configures the YouTube Channel Search Tool to fetch data from the specified channel. It sets up the model used for both the language processing and the embedding tasks.

## Acknowledgements
- Crew AI: For the framework that makes the orchestration of tasks seamless.
- LangChain Community: For providing tools for language model integrations.
- Ollama: For offering the model used in this project.

