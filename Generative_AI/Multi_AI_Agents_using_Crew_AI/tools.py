from crewai_tools import YoutubeChannelSearchTool



yt_tool =YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                temperature=0.5,
                # top_p=1,
                #stream=True,
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


