import re
import dateparser

from dateparser.search import search_dates


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

    try:

        result = search_dates(
            cleaned_text,

            languages=["es"],

            settings={

                "PREFER_DATES_FROM": "future",

                "TIMEZONE": "America/Lima",

                "RETURN_AS_TIMEZONE_AWARE": False,
            }
        )

        print("TEXTO:", cleaned_text)
        print("RESULTADO:", result)

        if result:
            return result[0][1]

        return None

    except Exception as e:

        print("ERROR FECHA:", e)

        return None


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

    if "pago" in text:
        return "payment"

    if "comprar" in text:
        return "shopping"

    if "estudiar" in text:
        return "study"

    return "general"