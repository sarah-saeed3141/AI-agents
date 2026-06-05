#AI Agent Conversations with AutoGen and Ollama

This project demonstrates how to build and run multiple AI agents locally using AutoGen and Ollama. The example included in this repository creates two stand-up comedian agents that engage in a conversation while maintaining conversational context and state.

##Features
- [X] Run AI agents locally using Ollama (No OpenAI API key required)
- [X] Create multiple agents with different personalities and roles
- [X] Simulate multi-turn conversations between agents
- [ ] Experiment with agent memory, termination conditions, and group chats (#TODO)

##Requirements
- Python 3.11+
- Ollama installed and running
- A locally available Ollama model (e.g., llama3, mistral)

##Installations

Install the required Python packages:
- pip install autogen-agentchat autogen-ext ollama
- Pull an Ollama model:
- ollama pull mistral
- Verify that Ollama is running:
ollama list

The agents will take turns generating responses until the configured termination condition is reached.

##Project Structure
```text
.
├── two_standup_comedians.py
└── README.md
```


##Learning Objectives

This project explores:

- Agent creation and configuration
- Multi-agent communication
- Conversation orchestration
- Local LLM deployment with Ollama
- The modern AutoGen AgentChat API

##Future Improvements
Add memory and long-term conversation history
Introduce tool-using agents
Create debate and collaboration scenarios
Add a summarizer or judge agent
Support multiple local models

##License
This project is intended for educational and experimentation purposes.