import re
import dateparser


def clean_text(text):

    text = text.lower().strip()

    useless_words = [
        "hasta",
        "el día",
        "la",
        "de",
        "con",
        "para",
    ]

    for word in useless_words:
        text = text.replace(word, "")

    return text


def extract_date(text):

    cleaned_text = clean_text(text)

    date = dateparser.parse(
        cleaned_text,
        languages=["es"],

        settings={

            "PREFER_DATES_FROM": "future",

            "TIMEZONE": "America/Lima",

            "RETURN_AS_TIMEZONE_AWARE": False,
        }
    )

    return date


def detect_type(text):

    text = text.lower().strip()

    if "idea" in text:
        return "idea"

    if "reunión" in text:
        return "meeting"

    if "examen" in text:
        return "exam"

    if "entrega" in text:
        return "delivery"

    if "tesis" in text:
        return "thesis"

    return "general"