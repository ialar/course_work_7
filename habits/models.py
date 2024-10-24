from django.db import models

from config.settings import AUTH_USER_MODEL as U

NULLABLE = {"null": "True", "blank": "True"}


class Habit(models.Model):
    IS_ENJOYABLE_CHOICES = {True: "Приятная", False: "Полезная"}
    PERIOD_CHOICES = {True: "Ежедневная", False: "Еженедельная"}
    PUBLIC_CHOICES = {True: "Публичная", False: "Личная"}

    owner = models.ForeignKey(U, on_delete=models.CASCADE, verbose_name="Пользователь")
    place = models.CharField(max_length=50, verbose_name="Место выполнения привычки")
    time = models.TimeField(max_length=25, verbose_name="Время, когда надо выполнить привычку")
    action = models.CharField(max_length=100, verbose_name="Действие, которое надо выполнить")
    duration = models.PositiveSmallIntegerField(verbose_name="Время на выполнение привычки", **NULLABLE)
    reward = models.CharField(max_length=50, verbose_name="Вознаграждение", **NULLABLE)
    related = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    is_enjoyable = models.BooleanField(default=True, choices=IS_ENJOYABLE_CHOICES, verbose_name="Приятная")
    is_daily = models.BooleanField(default=True, choices=PERIOD_CHOICES, verbose_name="Периодичность")
    is_public = models.BooleanField(default=True, choices=PUBLIC_CHOICES, verbose_name="Публичная")

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}.'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
