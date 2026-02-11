from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from .models import ContactMessage
from .schemas import ContactMessageCreate
from .db import get_db

contact_router = APIRouter(prefix="/api/contact")


@contact_router.post("/")
def contact(
    msg: ContactMessageCreate,
    db: Session = Depends(get_db)
):
    try:
        entry = ContactMessage(
            name=msg.name,
            email=msg.email,
            message=msg.message,
            timestamp=datetime.now(timezone.utc)
        )

        db.add(entry)
        db.commit()
        db.refresh(entry)

        return {"status": "received"}

    except Exception as e:
        print("❌ Contact error:", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to save contact message"
        )
