from crewai_tools import YoutubeChannelSearchTool
# import os
# from dotenv import load_dotenv

# load_dotenv()

#Initialize the tool with a specific Youtube channel handle to target your search
# yt_tool=YoutubeChannelSearchTool(youtube_channel_handle="@krishnaik06")


yt_tool =YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                temperature=0.5,
                # top_p=1,
                stream=True,
            ),
        ),
        embedder=dict(
            provider="ollama", # or openai, ollama, ...
            config=dict(
                model="llama2",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)

# yt_tool=tool(youtube_channel_handle="@krishnaik06")
