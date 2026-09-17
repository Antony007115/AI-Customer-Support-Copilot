import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.copilot import create_support_draft
from backend.validator import validate_draft

app = FastAPI(title="AI Customer Support Copilot")


class Ticket(BaseModel):
    ticket_id: str
    customer_name: str
    issue: str
    priority: str


class ReviewRequest(BaseModel):
    ticket_id: str
    action: str
    final_reply: str


@app.get("/")
def home():
    return {
        "message": "AI Customer Support Copilot is running"
    }


@app.post("/draft")
def create_draft(ticket: Ticket):
    try:
        raw_response = create_support_draft(ticket.model_dump())
        result = validate_draft(raw_response)

        if not result["valid"]:
            raise HTTPException(
                status_code=500,
                detail=result["error"]
            )

        return result["data"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/review")
def review_draft(review: ReviewRequest):
    if review.action not in ["APPROVE", "EDIT", "REJECT"]:
        raise HTTPException(
            status_code=400,
            detail="Action must be APPROVE, EDIT, or REJECT."
        )

    if review.action == "REJECT":
        status = "REJECTED"
    elif review.action == "EDIT":
        status = "EDITED_AND_APPROVED"
    else:
        status = "APPROVED"

    return {
        "ticket_id": review.ticket_id,
        "final_reply": review.final_reply,
        "review_action": review.action,
        "status": status
    }