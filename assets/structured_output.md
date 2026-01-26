### Structured Output
A practice of having LLM to return response in well structured format(for eg JSON) rather than free form text.

### Ways to get structured output
- There are 2 ways:
    - with_structured_output method
    - output parser

### with_structured_output
- This method require a data format.
- data format can be in TypeDict, pydantic, or json schema

### TypeDict
- It tell python what key are required and what type of value key should hold.
- It does not validate data at runtime.
- It just help with type hints.
- Lightweight extraction.
- syntax: summary: Annotated[str, "A brief summary of the product review."]

### Pydantic
- Validate the type at run time.
- Type conversion ('age':'32' -> it change string into number 'age':32)
- It provide built in functionality like EmailStr to validate email (email: EmailStr)
- It provide Feild function (eg: cgpa: float = Feild(gt=0, lt=10, default, description))
- It ensure data is structured and type-safe.
- For production pipelines.
- syntax: summary: Annotated[str, Field(description="A brief summary of the product review.")]

## Output Parser
### PydanticOutputParser
It enforce schema validation when processing LLM response.
- Ensure that LLM response follow a well defined structure.
- Presnet in langchain_core library
- from langchain_core.output_parser import PydanticOutputParser