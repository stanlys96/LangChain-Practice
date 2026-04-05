from langchain.agents import create_agent
from dotenv import load_dotenv
import pprint

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always rainy in {city}!"

agent = create_agent(
    model="openai:gpt-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
res = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

pprint.pprint(res)