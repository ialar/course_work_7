from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "place",
        "time",
        "action",
        "duration",
        "reward",
        "related",
        "frequency",
        "is_enjoyable",
        "is_public",
    )
    # list_filter = ("id", "owner", "is_public", "is_enjoyable")
