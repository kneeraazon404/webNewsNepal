# webNewsNepal

A web News Site for a Client

## Settings for static files and medias plus same goes for templates

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "newssite/static")]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"

## Ckeditor

pip install ckeditor
