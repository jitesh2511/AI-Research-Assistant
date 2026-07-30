from backend.llm.base import LLMProvider
from config import GEMINI_API_KEY, GEMINI_MODEL
from google import genai
from google.genai import errors
import logging

logger = logging.getLogger(__name__)

class GeminiProvider(LLMProvider):

    def __init__(self):
        if not GEMINI_API_KEY:
            logger.error("GEMINI_API_KEY is not configured")
            raise ValueError("GEMINI_API_KEY is not configured")
        if not GEMINI_MODEL:
            logger.error("GEMINI_MODEL is not configured")
            raise ValueError("GEMINI_MODEL is not configured")
        
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt:str) -> str:

        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )

            if response.text is None or response.text.strip() == "":
                logger.error("Gemini returned an empty response")
                raise ValueError("Gemini returned an empty response")
            
            logger.info("generated response successfully")
            return response.text
        
        except errors.APIError as e:
            logger.error(f"Gemini API Error ({e.code}): {e.message}")
            raise
            
        except ValueError:
            raise

        except Exception as e:
            logger.exception("unexpected error occured while generating response")
            raise

geminiProvider = GeminiProvider()