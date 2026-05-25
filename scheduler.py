from apscheduler.schedulers.background import BackgroundScheduler
from database import supabase
from telegram_utils import send_telegram_message

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

scheduler = BackgroundScheduler()

already_sent = set()


def check_reminders():

    peru_time = datetime.now(
        ZoneInfo("America/Lima")
    )

    next_hour = peru_time + timedelta(hours=1)

    response = (
        supabase
        .table("memories")
        .select("*")
        .not_.is_("reminder_date", None)
        .lte(
            "reminder_date",
            next_hour.isoformat()
        )
        .execute()
    )

    memories = response.data

    for memory in memories:

        memory_id = memory["id"]

        if memory_id in already_sent:
            continue

        send_telegram_message(
            f"⏰ Recordatorio:\n\n{memory['content']}"
        )

        already_sent.add(memory_id)


scheduler.add_job(
    check_reminders,
    "interval",
    minutes=5
)

scheduler.start()