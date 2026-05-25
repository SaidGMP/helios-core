from parser_utils import extract_date, detect_type
from database import supabase


def process_memory(content):

    content = content.strip()

    if not content:
        return None

    detected_date = extract_date(content)

    priority = "normal"

    urgent_words = [
        "urgente",
        "importante",
        "examen",
        "entrega"
    ]

    if any(word in content.lower() for word in urgent_words):
        priority = "high"

    memory_type = detect_type(content)

    data = {
        "content": content,
        "priority": priority,
        "type": memory_type,
        "reminder_date":
            detected_date.isoformat()
            if detected_date else None
    }

    response = (
        supabase
        .table("memories")
        .insert(data)
        .execute()
    )

    return {
        "detected_date": detected_date,
        "priority": priority,
        "type": memory_type,
        "data": response.data
    }