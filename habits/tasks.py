import pytz
from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_habit_message():
    habits = Habit.objects.all()
    now = timezone.now()
    moscow_tz = pytz.timezone('Europe/Moscow')
    formatted_time = now.astimezone(moscow_tz).strftime("%H:%M")
    print(formatted_time)

    for habit in habits:
        hm_habit_time = habit.time.strftime("%H:%M")
        print(hm_habit_time)
        if hm_habit_time == formatted_time:
            tg_chat = habit.owner.tg_chat_id
            message = f'Я буду {habit.action} в {habit.time} в {habit.place}.'
            send_tg_message(tg_chat, message)
