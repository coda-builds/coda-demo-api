from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/agent", tags=["Agent Demo"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    message = request.message.lower()

    if "opening" in message or "hours" in message or "open" in message:
        reply = "LondonFit Gym is open Monday to Friday from 6am to 10pm, and weekends from 8am to 8pm."
    elif "price" in message or "cost" in message or "student" in message or "membership" in message:
        reply = "The standard membership is £49/month. Students pay £35/month with a valid student ID."
    elif "freeze" in message or "pause" in message:
        reply = "Yes, members can freeze their membership for up to 3 months."
    elif "cancel" in message or "cancellation" in message:
        reply = "You can cancel with 30 days notice. I can collect your details and pass this to the support team."
    elif "trial" in message or "book" in message:
        reply = "Yes, you can book a free trial session. The team will need your name, phone number, and preferred date."
    else:
        reply = "I can help with opening hours, pricing, memberships, cancellations, freezes, and trial sessions."

    return ChatResponse(reply=reply)
