from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "competition",
        "team_leader_name",
        "roll_no",
        "phone",
        "num_participants",
        "submitted_at",
    )
    list_filter = ("competition", "submitted_at")
    search_fields = ("team_leader_name", "roll_no", "phone")
