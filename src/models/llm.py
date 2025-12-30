from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("What is the capital of Canada?")
print(result)