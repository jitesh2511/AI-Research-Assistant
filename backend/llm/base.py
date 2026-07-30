from abc import ABC, abstractmethod

class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:

        """Generate response from the given prompt"""

        return