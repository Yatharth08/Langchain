from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

prompt1 = PromptTemplate(
    input_variables=["text"],
    template = "Generate concise structured notes about:\n{text}"
)
prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Generate 5 quiz questions with answers based on:\n{text}"
)

prompt3 = PromptTemplate(
    input_variables=["notes", "quiz"],
    template="Merge the provided {notes} and {quiz} into a single coherent document"
)
llm = ChatOpenAI()
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    notes=prompt1 | llm | parser,
    quiz=prompt2 | llm | parser
)

merge_chain = prompt3 | llm | parser

chain = parallel_chain | merge_chain
result = chain.invoke({"text": """
    The CN Tower is a 553.3 m-high concrete communications and observation tower located in Downtown Toronto, Ontario, Canada. It was completed in 1976 and held the record for the world's tallest free-standing structure for 32 years until 2007. The tower is named after the Canadian National Railway, which originally owned it. It is one of Canada's most recognizable landmarks and a popular tourist destination, attracting over two million international visitors annually. The CN Tower features a revolving restaurant, observation decks, and the EdgeWalk, an outdoor walk on the roof of the main pod for thrill-seekers.
"""})

print(result)
# To visualize the chain structure
chain.get_graph().print_ascii()