from django.db import models

class Competition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    min_participants = models.IntegerField(default=1)
    max_participants = models.IntegerField(default=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
