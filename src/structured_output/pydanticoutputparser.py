from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated
import os
from dotenv import load_dotenv
load_dotenv()
class Person(BaseModel):
    name: Annotated[str, Field(description="The full name of the person.")]
    age: Annotated[int, Field(gt=18, description="The age of the person in years.")]
    city: Annotated[str, Field(description="The city where the person lives.")]

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)
model = ChatHuggingFace(llm=llm)

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser
final_output = chain.invoke({"place": "Italian"})
print("final output:", final_output)