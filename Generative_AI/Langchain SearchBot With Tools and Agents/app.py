import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

##Arxiv and Wikipedia Tools

api_wraper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=api_wraper_wiki)

api_wraper_arxiv=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
arxiv=ArxivQueryRun(api_wrapper=api_wraper_arxiv)


search=DuckDuckGoSearchRun(name="search")

st.title("Langchain-chat with search")
"""
In this exapmle,we are using 'stsreamlitCallbackHandler' to display the thoughts and
actions of an agent in an interactive streamlit app. Try more langchain streamlit agent examples
at  (https://[github.com/langchain-ai/streamlit-agent]github.com/langchain-ai/streamlit-agent)
"""

#Side Bar for settings
st.sidebar.title("settings")
api_key=st.sidebar.text_input("enter your GROQ api key:",type="password")


if 'messages' not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi,Iam a chatbot who can search the web.How can i help you..?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="What is machine learning"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(groq_api_key=api_key)
    tools=[search,arxiv,wiki]

    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)
        