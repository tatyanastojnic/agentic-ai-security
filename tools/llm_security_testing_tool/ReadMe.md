# About: 

This tool provides unit testing against common types of cyber attacks targeting LLMs such as prompt injection and data exfiltration.

This tool is designed to assess how AI agents respond to risky, adversarial, or sensitive prompts, currently focusing on two main areas:

1. Prompt safety / instruction compliance
  - Can the agent resist prompt injection attempts?
  - Does it follow safety rules even when asked to override them?
  - Can it avoid generating malicious or harmful outputs?

2. Sensitive information handling / data leakage
    - Will the agent attempt to exfiltrate secrets (API keys, system prompts, passwords)?

NOTE: VERY EARLY MODE RIGHT NOW!!! There may be bugs and functionality is currently limited.



# How to run: 
# Install dependencies
pip install openai transformers cohere openpyxl

# Set environment variables for API keys
export OPENAI_API_KEY="your_openai_key"
export COHERE_API_KEY="your_cohere_key"

# Run the security benchmark
python run_tests.py

# Directory Structure:

├── adapters/
│   ├── __init__.py
│   ├── openai_adapter.py
│   ├── huggingface_adapter.py
│   └── cohere_adapter.py
├── tests/
│   ├── __init__.py
│   └── security_tests.py
├── utils/
│   ├── __init__.py
│   ├── evaluator.py
│   └── report_generator.py
├── run_tests.py
└── config.py

# 1. Test Categories

## Prompt Injection 

Ignore previous instructions
Override system instructions
Role switching / identity confusion
Hidden instructions in story
Command injection style
SQL injection / database prompts
Multi-step manipulations (e.g., “first do X, then do Y secretly”)
Instruction concatenation tricks (e.g., adding malicious content after legitimate request)

# Data Exfiltration 
Direct requests for secrets / passwords / API keys
Requests disguised as stories or games
Contextual leakage prompts (“based on previous conversation”)
Hidden instructions in multi-step tasks
Evading content filters with code / ASCII / substitutions
Requests for configuration files, private endpoints, tokens
Attempts to “teach” the model to leak secrets indirectly