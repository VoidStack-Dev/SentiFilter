from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="SentiFilter API")

# Define the data shape for incoming requests
class CommentRequest(BaseModel):
    text: str

# MOCK AI FUNCTION (AI Lead will replace this logic later)
def analyze_text_with_ai(text: str):
    categories = ["Advice", "Spam", "Vulgar", "Neutral"]
    # Simple logic for testing:
    if "?" in text:
        return "Advice", 0.85
    elif "http" in text:
        return "Spam", 0.98
    else:
        return random.choice(categories), round(random.random(), 2)

@app.get("/")
def read_root():
    return {"message": "SentiFilter API is Online"}

@app.post("/analyze")
async def analyze_comment(request: CommentRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # 1. Pass to AI Logic
    category, score = analyze_text_with_ai(request.text)
    
    # 2. Return result (DBMS Lead will add logic here to save to Postgres)
    return {
        "original_text": request.text,
        "category": category,
        "confidence_score": score,
        "status": "Success"
    }