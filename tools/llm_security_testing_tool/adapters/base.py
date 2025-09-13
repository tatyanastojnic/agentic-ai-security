class LLMInterface:
    """Abstract interface for LLMs."""
    def call(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")
