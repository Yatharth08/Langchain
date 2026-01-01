### LLM:
- General pupose model used for any NLP task.
- Pure text-in → text-out models
- They predict the next token given previous text
- No built-in understanding of roles, turns, or conversation state


### Chat models:
- Specialized for conversational task
- Built on top of language models.
- Fine-tuned for conversation
- Understand roles, turns, and dialogue flow
- Take text as input and return ChatMessage object

### temperature:
- It control the randomness of the output
- Temperature value can be set between 0-2
- If temperature is 0, model will always give same answer to the given input
- if we keep increasing the temperature, even to 0.2 answer, llm will give
creative output.
- for maths, code, facts - lower temperature is preferred
- for general qa - mid range
- for story telling, jokes - 0.9 - 1
- for more randomness, use temperature > 1
- chat_model = ChatOpenAI(model="gpt-4", temperature=1.7)

### max_completions_tokens:
- controls the max length of the output
- Cost is dependent on the number of tokens used
- Higher the max_completion_tokens, higher the cost

### Open source and paid models.
- Model like openai, claude sonnet and gemeni and made by companies and are running on their server. We can access them using API keys but these models are paid and we can't change anything in them.
- Open source model like llama, mistral, falcon are available on internet that we can download(or use hugging face api key), fine tune and deploy anywhere. You can run them locally. You can fine tune model on our private database.
- Disadvantage: 
    - Require high resources - GPU
    - Setup is complex
    - Lack of RLHF - Most of open source model are not fine tuned with human feedback
