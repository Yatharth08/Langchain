from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4")
message =  [
    SystemMessage(content="You are a helpfull assistant"),
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    message.append(HumanMessage(content=user_input))
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("AI: ", response.content)
