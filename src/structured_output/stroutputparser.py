from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)
model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="write a detailed report about {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="Give summary about {text}",
    input_variables=["text"]
)
# prompt1 = template1.invoke({"topic": "Artificial Intelligence"})
# response1 = model.invoke(prompt1)
# prompt2 = template2.invoke({"text": response1.content})
# response2 = model.invoke(prompt2)
# print("Summary:", response2.content)

parser = StrOutputParser()

chain = template1 | model | parser| template2 | model | parser
response = chain.invoke({'topic': 'Artificial Intelligence'})
print("Final Summary:", response)