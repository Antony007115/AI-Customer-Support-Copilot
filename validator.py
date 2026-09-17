import json


def validate_draft(response):
    try:
        # Remove Markdown code fences if Gemini adds them
        response = response.strip()

        if response.startswith("```"):
            response = response.replace("```json", "", 1)
            response = response.replace("```", "", 1)
            response = response.strip()

        data = json.loads(response)

        required_fields = [
            "ticket_id",
            "draft_reply",
            "grounded",
            "review_status"
        ]

        for field in required_fields:
            if field not in data:
                return {
                    "valid": False,
                    "error": f"Missing field: {field}"
                }

        if data["review_status"] != "PENDING_REVIEW":
            return {
                "valid": False,
                "error": "Draft must require human review."
            }

        return {
            "valid": True,
            "data": data
        }

    except json.JSONDecodeError:
        return {
            "valid": False,
            "error": "Gemini returned invalid JSON."
        }