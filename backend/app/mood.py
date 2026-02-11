from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from .schemas import MoodCheckIn
from .models import MoodEntry
from .auth import get_current_user
from .db import get_db

mood_router = APIRouter(prefix="/api/mood")


@mood_router.post("/checkin")
def checkin(
    mood: MoodCheckIn,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        entry = MoodEntry(
            user_id=user.id,
            mood=mood.mood,
            note=mood.note,
            timestamp=datetime.now(timezone.utc)
        )

        db.add(entry)
        db.commit()
        db.refresh(entry)

        return {
            "status": "saved",
            "id": entry.id,
            "mood": entry.mood,
            "note": entry.note,
            "timestamp": entry.timestamp.isoformat()
        }

    except Exception as e:
        print("❌ Mood save error:", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to save mood entry"
        )


@mood_router.get("/trends")
def get_mood_trends(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    try:
        moods = (
            db.query(MoodEntry)
            .filter(MoodEntry.user_id == user.id)
            .order_by(MoodEntry.timestamp.asc())
            .all()
        )

        data = []
        for m in moods:
            data.append({
                "id": m.id,
                "mood": m.mood,
                "note": m.note or "",
                "timestamp": m.timestamp.isoformat(),
                "date": m.timestamp.strftime("%Y-%m-%d")
            })

        return {
            "count": len(data),
            "data": data
        }

    except Exception as e:
        print("❌ Mood fetch error:", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch mood trends"
        )
