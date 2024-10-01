from crewai import Agent,LLM
from tools import yt_tool
from langchain_community.llms import Ollama



#Create a senior blog content researcher

blog_researcher=Agent(
    role="Blog researcher from youtube videos",
    goal="get the relevent video transcription for the topic {topic} from the provided Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos AI Data Science , Machine Learning And GEN AI providing suggestion"
    ),
    tools=[yt_tool],
    llm=LLM(model="ollama/llama2", base_url="http://localhost:11434"),
    allow_delegation=True
    

)
## Creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YT video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics,you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=LLM(model="ollama/llama2", base_url="http://localhost:11434"),
    allow_delegation=False
    
)
