from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")
        email = os.getenv("ADMIN_EMAIL", "")

        if not username or not password:
            print("ADMIN ENV VARS NOT SET")
            return

        if User.objects.filter(username=username).exists():
            print("ADMIN ALREADY EXISTS")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("ADMIN CREATED")
