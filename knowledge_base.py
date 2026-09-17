from pathlib import Path


KNOWLEDGE_FILE = Path("data/knowledge/approved_knowledge.txt")


def load_approved_knowledge():
    """Load only the approved support knowledge."""
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError("Approved knowledge base not found.")

    return KNOWLEDGE_FILE.read_text(encoding="utf-8")