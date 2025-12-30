### What are prompt?
- Prompt are instruction or queries given to model to guide its model.

### Classification of prompts
- Static: A static prompt is fixed and hard-coded. It does not change based on user input, context, or retrieved data.
- Dynamic: A dynamic prompt is constructed at runtime using user input

### Types of prompt
- Instruction Prompt: Directly tells the model what to do.
    - Example: Explain cosine similarity in simple terms.
- Question Prompt: Asks a question without explicit instructions
    - Example: What is the difference between TF-IDF and BM25? 
- Zero-Shot Prompt: No examples are provided—just the task.
    - Example: Classify this text as positive or negative: "The model works surprisingly well."
- Few-Shot Prompt: Includes a few examples to guide the model.
    - Example:  Text: “I love this movie” → Sentiment: Positive
                Text: “This is terrible” → Sentiment: Negative
                Text: “The product is okay” → Sentiment: ?
- Chain-of-Thought Prompt: Encourages step-by-step reasoning.
    - Solve this step by step: If a house costs $800k and increases by 5% annually, what is the price after 2 years?
- Role-Based Prompt: Assigns a role to the model.
    - Example: You are a senior data scientist. Explain embeddings to a beginner.

### PromptTemplate
- Structed way in langchain to create prompts dynamically by inserting variable into predefined templates. Instead of hardcoding, PromptTemplate allow to define placeholders that can be filled in runtime.

### Why PromptTemplate over f string?
- Validated variables
- Reusable templates

### Prompt to messages
#### PromptTemplate
- returns plain text (StringPromptValue)
- LangChain automatically wraps it as
HumanMessage(content=prompt.text) when sending to a chat model

#### ChatPromptTemplate
- returns structured chat messages (ChatPromptValue)
- LangChain sends those messages as-is (system / human / ai roles preserved)

PromptTemplate
   ↓ invoke()
StringPromptValue (just text)
   ↓ passed to ChatOpenAI
Converted to HumanMessage
   ↓ sent to GPT-4
AIMessage returned
 