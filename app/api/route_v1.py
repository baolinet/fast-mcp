from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.ai.agent import SmartAgent

router = APIRouter()

@router.get("/agent/ask")
def ask_agent(q: str) -> dict:
    agent = SmartAgent()
    answer = agent.answer(q)
    return {"question": q, "answer": answer}

@router.get("/agent/ask2")
def ask_agent_stream(q: str):
    agent = SmartAgent()
    generator = agent.stream_answer(q)
    return StreamingResponse(generator, media_type="text/plain") 