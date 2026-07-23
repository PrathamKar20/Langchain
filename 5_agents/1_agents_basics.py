from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import Client
from langchain.agents import create_agent
import datetime
from langchain_core.tools import tool

# Load environment variables from .env
load_dotenv()

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

# Create a ChatOpenAI model (using modern model)
llm = ChatOpenAI(model="gpt-4o")

query = "What is the current time in London? (You are in India). Just show the current time and not the date"

# In modern LangChain, we pull prompts using the Client from the langsmith package
hub_client = Client()
prompt_template = hub_client.pull_prompt("hwchase17/react")

tools = [get_system_time]

# Using modern create_agent (which compiles to a graph with tool calling support)
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use tools when needed."
)

# Run the agent directly by passing messages
result = agent.invoke({"messages": [{"role": "user", "content": query}]})

# Output the final message content from the response
print(result["messages"][-1].content)