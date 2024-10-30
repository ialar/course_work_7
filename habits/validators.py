from rest_framework.serializers import ValidationError


class RewardOrRelatedValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        reward, related = habit.get("reward"), habit.get("related")
        if reward and related:
            raise ValidationError(
                "За выполнение может быть либо вознаграждение, либо связанная привычка."
            )


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get("duration") and habit.get("duration") > 120:
            raise ValidationError(
                "Время выполнения привычки должно быть не больше 2 минут."
            )


class IsRelatedEnjoyableValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get("related"):
            if not habit.get("related").is_enjoyable:
                raise ValidationError("Связанная привычка может быть только приятной.")


class IsEnjoyableRelatedValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        reward, related = habit.get("reward"), habit.get("related")
        if habit.get("is_enjoyable"):
            if reward or related:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки."
                )


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get("frequency"):
            if habit.get("frequency") < 1:
                raise ValidationError(
                    "За неделю необходимо выполнить привычку хотя бы один раз."
                )
