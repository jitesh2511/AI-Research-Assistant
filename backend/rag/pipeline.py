from backend.services.retrieval import search_query as search
from backend.rag.prompt import build_prompt
from backend.llm.gemini_provider import geminiProvider
from data_models.models import AnswerResponse

def generate_answer(query: str) -> dict:

    retrievalResult = search(query)

    if not retrievalResult:
        return AnswerResponse(
            answer="Retrieval could not find any similar chunks",
            sources=[]
        )

    prompt = build_prompt(query, retrievalResult.sources)
    response = geminiProvider.generate(prompt)

    return AnswerResponse(
        answer=response,
        sources=retrievalResult.sources
    )