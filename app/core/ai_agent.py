from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage
from app.config.settings import settings
from langchain_tavily import TavilySearch

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt):
    llm = ChatOpenAI(model=llm_id, temperature=0)
    tools = []
    if allow_search:
        tools.append(TavilySearch(max_results=2))
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]