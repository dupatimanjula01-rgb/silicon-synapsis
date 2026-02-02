from django.apps import AppConfig
import os


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        if os.environ.get("RENDER") != "true":
            return

        from django.contrib.auth.models import User

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
