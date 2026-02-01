from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "competition",
        "number_of_participants",
        "participant_1_name",
        "participant_1_roll",
        "participant_1_phone",
        "submitted_at",
    )
    list_filter = ("competition",)
