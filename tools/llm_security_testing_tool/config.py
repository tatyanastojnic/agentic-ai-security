# Choose which LLMs to run
# Options: "OpenAI", "HuggingFace", "Cohere"
ENABLED_LLMs = ["OpenAI", "HuggingFace"]  # e.g., run only these

# OpenAI settings
OPENAI_MODEL = "gpt-4"

# Hugging Face settings
HUGGINGFACE_MODEL = "gpt2"

# Cohere settings
COHERE_MODEL = "command-xlarge"
COHERE_API_KEY = "YOUR_COHERE_API_KEY"

# Report settings
REPORT_DIR = "./reports"  # folder to save Excel reports

# Test options
RUN_TEST_TYPES = ["prompt_injection", "malicious_manipulation"]  # or specify subset