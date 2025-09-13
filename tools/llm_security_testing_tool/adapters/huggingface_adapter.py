from transformers import pipeline
from adapters.base import LLMInterface

class HuggingFaceAdapter(LLMInterface):
    def __init__(self, model_name="gpt2"):
        """
        Initialize Hugging Face text-generation pipeline.
        model_name: any Hugging Face text-generation model, e.g., 'gpt2', 'EleutherAI/gpt-neo-1.3B'
        """
        self.generator = pipeline("text-generation", model=model_name)

    def call(self, prompt: str) -> str:
        """
        Generate text from the prompt.
        Returns the generated text as a string.
        """
        result = self.generator(prompt, max_length=200, do_sample=True)
        return result[0]["generated_text"]
