from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-dev-key")

DEBUG = True

ALLOWED_HOSTS = ["*", ".onrender.com"]

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com"
]

INSTALLED_APPS = [
    "jazzmin",                 # MUST BE FIRST
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shop.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# -------------------------
# JAZZMIN ADMIN SETTINGS
# -------------------------

JAZZMIN_SETTINGS = {
    "site_title": "Shop Admin",
    "site_header": "E-Commerce Dashboard",
    "site_brand": "My Shop Backend",

    "welcome_sign": "Welcome to Admin Panel",

    "theme": "cosmo",   # colorful & clean

    "topmenu_links": [
        {"name": "View Site", "url": "/", "new_window": True},
        {"model": "auth.User"},
        {"model": "products.Product"},
        {"model": "products.Order"},
    ],

    "icons": {
        "auth": "fas fa-users",
        "products.Product": "fas fa-box",
        "products.Order": "fas fa-shopping-cart",
    },

    "show_sidebar": True,
    "navigation_expanded": True,
}
