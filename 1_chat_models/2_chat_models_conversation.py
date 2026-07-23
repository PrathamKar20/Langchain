from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm= ChatOpenAI(model="gpt-4o")
messages=[
    SystemMessage(content="You are an expert in social media content strategy"),
    HumanMessage(content="Give some helpful tips for viral posts on instagram")
]

result=llm.invoke(messages)
print(result)