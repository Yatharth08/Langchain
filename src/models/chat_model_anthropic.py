from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_anthropic = ChatAnthropic(model="claude-3.5-sonnet-20241022")
response = chat_anthropic.invoke("Write a short story about a robot learning to love.")
print(response.content)