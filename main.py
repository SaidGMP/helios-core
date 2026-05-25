import scheduler

from telegram_utils import send_telegram_message

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from database import supabase
from memory_service import process_memory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "API funcionando"
    }


class Memory(BaseModel):
    content: str


@app.post("/memories")
def create_memory(memory: Memory):

    result = process_memory(
        memory.content
    )

    if not result:

        return {
            "message": "Empty memory"
        }

    send_telegram_message(
        f"🧠 Nueva memoria guardada:\n\n{memory.content}"
    )

    return {
        "message": "Memory saved",
        **result
    }


@app.get("/memories")
def get_memories():

    response = (
        supabase
        .table("memories")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return response.data


@app.get("/test-telegram")
def test_telegram():

    send_telegram_message(
        "🚀 HELIOS conectado correctamente."
    )

    return {
        "message": "Telegram sent"
    }