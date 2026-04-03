from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import os
from nlp_engine import get_engine

app = FastAPI(title="NLP Insight API", description="API for Summarization and Sentiment Analysis")

# Add CORS middleware to allow requests from our Vue/React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str

class SentimentResponse(BaseModel):
    label: str
    score: float

class FullAnalysisResponse(BaseModel):
    summary: str
    sentiment: SentimentResponse

@app.on_event("startup")
async def startup_event():
    # Warm up / initialize the NLP engine when the application starts
    get_engine()

@app.post("/api/summarize", response_model=SummarizeResponse)
async def summarize(request: TextRequest):
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    engine = get_engine()
    summary = engine.summarize_text(request.text)
    return SummarizeResponse(summary=summary)

@app.post("/api/sentiment", response_model=SentimentResponse)
async def sentiment(request: TextRequest):
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    engine = get_engine()
    result = engine.analyze_sentiment(request.text)
    return SentimentResponse(label=result["label"], score=result["score"])

@app.post("/api/analyze", response_model=FullAnalysisResponse)
async def analyze_full(request: TextRequest):
    """Convenience endpoint to perform both summarization and sentiment analysis simultaneously"""
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    engine = get_engine()
    summary = engine.summarize_text(request.text)
    sentiment = engine.analyze_sentiment(request.text)
    
    return FullAnalysisResponse(
        summary=summary,
        sentiment=SentimentResponse(label=sentiment["label"], score=sentiment["score"])
    )

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# Mount frontend static files
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
frontend_dir = os.path.join(parent_dir, "frontend")
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
