from django.contrib import admin
from .models import Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "min_participants",
        "max_participants",
        "created_at",
    )

    list_filter = ("created_at",)
    search_fields = ("title",)
