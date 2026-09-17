from backend.llm import generate_reply
from backend.knowledge_base import load_approved_knowledge


def create_support_draft(ticket):
    knowledge = load_approved_knowledge()

    prompt = f"""
You are an AI Customer Support Copilot for ACME Support Services.

Your job is to draft a customer support reply.

IMPORTANT RULES:
1. Use ONLY the approved knowledge provided below.
2. Do not invent policies, refunds, compensation, timelines, or actions.
3. If the information is unavailable, clearly say so.
4. Be polite, professional, and concise.
5. Return ONLY valid JSON.

APPROVED KNOWLEDGE:
{knowledge}

CUSTOMER TICKET:
Ticket ID: {ticket["ticket_id"]}
Customer: {ticket["customer_name"]}
Issue: {ticket["issue"]}
Priority: {ticket["priority"]}

Return this JSON structure:
{{
    "ticket_id": "{ticket["ticket_id"]}",
    "draft_reply": "your support reply",
    "grounded": true,
    "review_status": "PENDING_REVIEW"
}}
"""

    return generate_reply(prompt)