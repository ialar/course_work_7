from rest_framework import serializers

from habits.models import Habit
from habits.validators import (DurationValidator, FrequencyValidator,
                               IsEnjoyableRelatedValidator,
                               IsRelatedEnjoyableValidator,
                               RewardOrRelatedValidator)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardOrRelatedValidator(field="reward"),
            DurationValidator(field="duration"),
            IsRelatedEnjoyableValidator(field="related"),
            IsEnjoyableRelatedValidator(field="is_enjoyable"),
            FrequencyValidator(field="frequency"),
        ]
