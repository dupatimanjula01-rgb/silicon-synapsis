from django.db import models
from competitions.models import Competition

class Registration(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    number_of_participants = models.IntegerField()

    participant_1_name = models.CharField(max_length=100)
    participant_1_roll = models.CharField(max_length=50)
    participant_1_phone = models.CharField(max_length=15)

    participant_2_name = models.CharField(max_length=100, blank=True, null=True)
    participant_2_roll = models.CharField(max_length=50, blank=True, null=True)
    participant_2_phone = models.CharField(max_length=15, blank=True, null=True)

    participant_3_name = models.CharField(max_length=100, blank=True, null=True)
    participant_3_roll = models.CharField(max_length=50, blank=True, null=True)
    participant_3_phone = models.CharField(max_length=15, blank=True, null=True)

    participant_4_name = models.CharField(max_length=100, blank=True, null=True)
    participant_4_roll = models.CharField(max_length=50, blank=True, null=True)
    participant_4_phone = models.CharField(max_length=15, blank=True, null=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.competition.title}"
