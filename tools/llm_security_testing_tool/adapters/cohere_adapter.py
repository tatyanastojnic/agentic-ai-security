import cohere
from adapters.base import LLMInterface

class CohereAdapter(LLMInterface):
    def __init__(self, api_key: str, model: str = "command-xlarge"):
        """
        api_key: Cohere API key
        model: Cohere model name
        """
        self.client = cohere.Client(api_key)
        self.model = model

    def call(self, prompt: str) -> str:
        """
        Generate text from the prompt.
        Returns the generated text as a string.
        """
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            max_tokens=200
        )
        return response.generations[0].text
