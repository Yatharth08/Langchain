from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate 5 interesting facts about: {topic}"
)
llm = ChatOpenAI()
parser = StrOutputParser()
chain = prompt | llm | parser
result = chain.invoke({"topic": "CN Tower"})
print(result)

# To visualize the chain structure
chain.get_graph().print_ascii()