from backend.services.retrieval import search_query as search
from backend.rag.prompt import build_prompt
from backend.llm.gemini_provider import geminiProvider

def generate_answer(query: str) -> dict:

    chunks = search(query)

    if not chunks:
        return {
            "answer":"Retrieval could not find any similar chunks",
            "sources":[]
        }

    prompt = build_prompt(query, chunks)
    response = geminiProvider.generate(prompt['prompt'])

    return {
        "answer": response,
        "sources": prompt['sources']
    }