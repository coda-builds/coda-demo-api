from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/rag", tags=["Document Assistant Demo"])


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    source: str


@router.post("/query", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    question = request.question.lower()

    if "refund" in question:
        return QueryResponse(
            answer="Customers can request a refund within 14 days of purchase if the service has not started.",
            source="Refund Policy, Section 2",
        )

    if "holiday" in question or "leave" in question or "annual" in question:
        return QueryResponse(
            answer="Full-time employees receive 25 days of paid annual leave plus UK bank holidays.",
            source="Employee Handbook, Section 4",
        )

    if "support" in question or "escalate" in question or "customer" in question:
        return QueryResponse(
            answer="Support agents should confirm the customer ID, check eligibility, and escalate refund requests over £500.",
            source="Support Playbook, Section 3",
        )

    if "onboarding" in question or "new employee" in question:
        return QueryResponse(
            answer="New employees complete account setup, security training, team onboarding, and their first manager check-in during week one.",
            source="Onboarding Guide, Section 1",
        )

    return QueryResponse(
        answer="I can answer questions about refunds, employee leave, onboarding, and support procedures from the sample documents.",
        source="Demo document set",
    )
