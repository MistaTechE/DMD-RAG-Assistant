# rag.py

from typing import List, Dict


def retrieve_chunks(question: str) -> List[str]:
    """
    TODO:
    - Replace this with Chroma vector DB search
    - Return top-k relevant PDF chunks based on semantic similarity
    """

    # Fake data for now so the pipeline works end-to-end
    return [
        "Gabapentin is frequently used for pain relief",
    ]


def build_prompt(question: str, chunks: List[str]) -> str:
    """
    TODO:
    - Improve prompt formatting for medical grounding related to DMD
    - Add citation formatting (source + page number later), should be easy to click and reach source
    """

    context = "\n\n".join(chunks)

    return f"""
You are a research assistant for Duchenne Muscular Dystrophy (DMD).

Answer ONLY using the context below.
If the answer is not in the context, say "Not enough evidence in provided sources."

Context:
{context}

Question:
{question}

Answer clearly and include references to the context.
"""


def call_llm(prompt: str) -> str:
    """
    TODO:
    - Replace with Gemma 27B / TxGemma inference
    - Run via Hugging Face or API endpoint
    """

    return "TODO: LLM not connected yet"


def generate_answer(question: str) -> Dict:
    """
    Main RAG pipeline:
    1. retrieve relevant chunks
    2. build prompt
    3. call LLM
    """

    chunks = retrieve_chunks(question)
    prompt = build_prompt(question, chunks)
    answer = call_llm(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": chunks
    }
