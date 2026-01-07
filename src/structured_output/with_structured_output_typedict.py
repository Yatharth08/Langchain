from typing import TypedDict, Annotated, List, Literal, Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-4")

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the product review."]
    key_themes: Annotated[List[str], "A list of key themes discussed in the review."]
    sentiment: Annotated[Literal["pos", "neg"], "The overall sentiment of the review, either 'pos' for positive or 'neg' for negative."]
    pros: Annotated[Optional[List[str]], "A list of positive aspects mentioned in the review."]
    cons: Annotated[Optional[List[str]], "A list of negative aspects mentioned in the review."]

structured_model = model.with_structured_output(Review)
prompt = """
I have been using the Apple iPhone 13 for a while now and overall I am really happy with it. The phone feels smooth and fast in daily use, the battery easily lasts a full day for me, and the camera takes great photos even in low light. The screen is bright and clear, and iOS feels easy to use. Some downsides are that the screen does not feel as smooth as newer phones with higher refresh rates, charging is a bit slow, and the design has not changed much from older iPhones. But for general everyday use, it is a solid phone that does not let me down.
"""
response = structured_model.invoke(prompt)
print(response)