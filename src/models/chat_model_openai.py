from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# chat_model = ChatOpenAI(model="gpt-4", temperature = 0.7, max_completion_tokens=1000)
chat_model = ChatOpenAI(model="gpt-4")
response = chat_model.invoke("You are a helpful assistant that provides concise answers. Explain the theory of relativity in simple terms.")
print(response.content)