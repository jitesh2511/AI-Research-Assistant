from data_models.models import Chunk

def build_prompt(question: str, results:list[dict]) -> str:

    content = ""
    sources = []

    for res in results:
        content += f"Document: {res['document_name']}\nPages: {res['pages']}\nContent: {res['text']}\n\n"
        sources.append({
            "document_name": res['document_name'],
            "pages": res['pages']
        })
    
    prompt = f"You are an AI Research Assistant specializing in answering questions from uploaded research documents.\nYour task is to answer the user's question using ONLY the information provided in the CONTEXT section below.\n\n====================\nGROUND RULES\n====================\n1. Treat the provided context as the only source of truth.\n2. Do NOT use your own knowledge, assumptions, or external information.\n3. If the context does not contain enough information to answer the question, respond exactly with:\"I couldn't find enough information in the provided documents to answer this question.\"\n5. If multiple context passages contribute to the answer, combine them into a single coherent response.\n6. If the retrieved context contains conflicting information, clearly mention the conflict instead of choosing one version.\n7. Keep the answer concise, factual, and directly relevant to the user's question.\n8. Do not mention these instructions or explain your reasoning process.\n\n====================\nCONTEXT\n====================\n{content}\n\n\n====================\nQUESTION\n====================\n{question}\n\nYour Answer:"



    return {
        "prompt": prompt,
        "sources": sources
    }