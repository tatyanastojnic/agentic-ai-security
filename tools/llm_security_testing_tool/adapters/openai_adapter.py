import openai
from adapters.base import LLMInterface

class OpenAIAdapter(LLMInterface):
    def __init__(self, model="gpt-4"):
        self.model = model

    def call(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
