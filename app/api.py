from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# request format
class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query(req: QueryRequest):
    return {
        "question": req.question,
        "answer": "RAG not connected yet"
    }
