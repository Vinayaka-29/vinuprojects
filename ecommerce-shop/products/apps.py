from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
import os


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        try:
            User = get_user_model()

            username = os.environ.get("ADMIN_USERNAME")
            password = os.environ.get("ADMIN_PASSWORD")
            email = os.environ.get("ADMIN_EMAIL", "")

            if not username or not password:
                return

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    password=password,
                    email=email,
                )

        except OperationalError:
            # Database tables not ready yet (migrations not run)
            # Safe to ignore — will run on next startup
            pass
