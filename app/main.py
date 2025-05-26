from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .agents.tutor_agent import tutor_agent

app = FastAPI(
    title="Multi-Agent Tutoring Bot",
    description="A tutoring system that helps with math and physics questions using specialized agents.",
    version="1.0.0"
)

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

@app.post("/ask", response_model=Answer)
async def ask_question(question: Question):
    """
    Ask a math or physics question to the tutoring system.
    
    The system will automatically detect whether the question is related to math or physics
    and route it to the appropriate specialized agent for processing.
    """
    if not question.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        answer = await tutor_agent.process_question(question.question)
        return Answer(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """
    Root endpoint that provides basic information about the API.
    """
    return {
        "name": "Multi-Agent Tutoring Bot",
        "version": "1.0.0",
        "description": "A tutoring system that helps with math and physics questions.",
        "endpoints": {
            "/ask": "POST endpoint to ask questions",
            "/": "GET endpoint for API information"
        }
    } 