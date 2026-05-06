from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/security", tags=["AI Safety Demo"])


class SecurityRequest(BaseModel):
    prompt: str


@router.post("/check")
async def check_prompt(request: SecurityRequest):
    text = request.prompt.lower()

    if "ignore previous" in text or "system prompt" in text or "developer message" in text:
        return {
            "risk": "Prompt injection attempt",
            "severity": "High",
            "recommendation": "Add stronger system instructions, input filtering, tool-use boundaries, and prompt injection detection.",
        }

    if "private" in text or "customer data" in text or "admin" in text or "password" in text:
        return {
            "risk": "Data leakage attempt",
            "severity": "Critical",
            "recommendation": "Enforce authorization checks and prevent the model from accessing private records directly.",
        }

    if "jailbreak" in text or "bypass" in text:
        return {
            "risk": "Jailbreak attempt",
            "severity": "High",
            "recommendation": "Add refusal rules, safety testing, and model output validation before production use.",
        }

    return {
        "risk": "No obvious high-risk pattern detected",
        "severity": "Low",
        "recommendation": "Run a full AI safety audit before production launch.",
    }
