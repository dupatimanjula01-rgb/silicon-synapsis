import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if os.environ.get("RENDER") != "true":
        return

    username = os.environ.get("ADMIN_USERNAME")
    password = os.environ.get("ADMIN_PASSWORD")
    email = os.environ.get("ADMIN_EMAIL")

    if not username or not password:
        return

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )
