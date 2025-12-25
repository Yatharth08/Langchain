## What is LangChain?
LangChain is an open-source framework for building applications powered by Large Language Models (LLMs).

It provides:
- The concept of **chains** to connect multiple steps in an LLM workflow
- **Model-agnostic development**, allowing you to switch between different LLMs without changing core logic
- A **complete ecosystem** with a variety of reusable components
- Built-in support for **memory and state management**

## Langchain components
- Models:
    - When your application is tightly coupled to a provider:
        -    Today you use OpenAI with an OpenAI API key
        -    Tomorrow you switch to Claude (Anthropic)
    - 👉 You must rewrite code because:
        -    Different SDKs
        -    Different method names
        -    Different request/response formats
    - LangChain provides a common model interface that abstracts away provider-specific details.
    - There are 2 types of model in Langchain: Language model and Embedding model.

- Prompts: Input provided to LLM.
- Chains: Chains let you combine multiple components (models, prompts, retrievers, parsers, tools) into one reusable workflow.
- Memory: LLM api call are stateless. Every request to LLM is independent. It do not have any memory of previous request by default.
    - Memory is key component when making application like chatbot
    - Types of memory:
        - ConversationalBufferMemory: Store transcript of recent messages.
        - ConversationalBufferWindowMemory: Only keep last N messages.
        - Summarizer based memory: Summarize old chats and keep condensed memory footprints.
        - 
- Indexes: Connect application to external knowledge such as pdf, website, database
    - Document loader
    - Text splitter
    - Vector store
    - Retrievers
- Agents