# AI Customer Support Copilot

An AI-powered customer support assistant that generates grounded support replies using customer ticket context and approved company knowledge.

## Objective

The system helps support agents create accurate draft replies while keeping a human reviewer in control of the final response.

## Workflow

Customer Ticket -> Approved Knowledge Base -> Gemini LLM -> Draft Support Reply -> JSON Validation -> Human Review -> Approve / Edit / Reject -> Final Reply

## Key Features

- Customer ticket processing
- Approved knowledge grounding
- Gemini-based response generation
- Structured JSON output
- Output validation
- Human review workflow
- Approve, Edit and Reject actions
- Hallucination control
- Handling of unavailable information
- Evaluation test cases

## Technology Stack

- Python
- FastAPI
- Gemini API
- Pydantic
- python-dotenv
- Uvicorn

## Evaluation

Five representative customer-support and safety test cases were executed. All five evaluation test cases passed.

## Safety Controls

- Uses only approved knowledge.
- Avoids unsupported claims.
- Does not invent refund amounts or policies.
- Clearly communicates when information is unavailable.
- Requires human review before final approval.

## Limitations

- Uses a simulated support company and knowledge base.
- Human review is required before sending a response.
- No production database or authentication is implemented.
- Review history is not persisted.

## Running the Project

uvicorn backend.api:app --reload

Swagger: http://127.0.0.1:8000/docs

