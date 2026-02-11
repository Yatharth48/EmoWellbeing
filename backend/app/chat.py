from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schemas import ChatRequest
from .models import ChatMessage
from .db import get_db
from .auth import get_current_user
from .hf_sentiment import analyze_sentiment
from .llm_client import generate_ai_reply

chat_router = APIRouter(prefix="/api/chat")


@chat_router.post("/send")
def send_message(
    data: ChatRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user),
):
    """
    Accepts a chat message from an authenticated user,
    analyzes sentiment, generates AI reply,
    stores chat in MySQL and returns it.
    """

    if not user or not user.id:
        raise HTTPException(status_code=401, detail="Invalid user credentials")

    try:
        sentiment, confidence = analyze_sentiment(data.message)
        ai_reply = generate_ai_reply(data.message)

        chat = ChatMessage(
            user_id=user.id,
            message=data.message,
            response=ai_reply,
            sentiment=sentiment,
            confidence=float(confidence),
        )

        db.add(chat)
        db.commit()
        db.refresh(chat)

        return {
            "id": chat.id,
            "user_id": chat.user_id,
            "message": chat.message,
            "response": chat.response,
            "sentiment": chat.sentiment,
            "confidence": chat.confidence,
            "timestamp": chat.timestamp.isoformat()
        }

    except Exception as e:
        print("❌ Chat error:", e)
        raise HTTPException(status_code=500, detail="Failed to process message")
