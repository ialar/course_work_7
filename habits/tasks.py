from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_habit_message():
    habits = Habit.objects.all()
    now = timezone.now().time().strftime("%H:%M")
    # print(now)

    for habit in habits:
        hm_habit_time = habit.time.strftime("%H:%M")
        # print(hm_habit_time)
        if hm_habit_time == now:
            tg_chat = habit.owner.tg_chat_id
            message = f'Я буду {habit.action} в {habit.time} в {habit.place}.'
            send_tg_message(tg_chat, message)
