from rest_framework.serializers import ValidationError


class HabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get("related") and habit.get("reward"):
            raise ValidationError("Может быть одно из двух: либо связанная привычка, либо вознаграждение.")
        if habit.get("duration") and habit.get("duration") > 120:
            raise ValidationError("Время выполнения привычки должно быть не больше 2 минут.")
        if habit.get("related"):
            if not habit.get("related").is_enjoyable:
                raise ValidationError("Связанная привычка может быть только приятной.")
        if habit.get("is_enjoyable").reward or habit.get("is_enjoyable").related:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
        if habit.get("frequency") < 1:
            raise ValidationError("За неделю необходимо выполнить привычку хотя бы один раз.")
