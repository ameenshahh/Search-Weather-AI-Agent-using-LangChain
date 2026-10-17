import os
import certifi
import requests
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub


from langchain.agents import create_react_agent, AgentExecutor


os.environ["SSL_CERT_FILE"] = certifi.where()
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

search_tool = TavilySearchResults(max_results=4)



result = search_tool.invoke("Give me the latest news on ai")
result

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

response = llm.invoke("What is the latest news on ai?")
response


prompt = hub.pull("hwchase17/react")
prompt


tools = [search_tool]
# tools = []

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agent_executor.invoke({
    "input":( 
        "Find the capital of India"
        "and then find its current weather"
        # "find the latest news on iran and us war"
    )
    })
response