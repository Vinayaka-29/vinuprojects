from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        User = get_user_model()

        username = os.environ.get("ADMIN_USERNAME")
        
        password = os.environ.get("ADMIN_PASSWORD")

        if not username or not password:
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                
                password=password
            )
