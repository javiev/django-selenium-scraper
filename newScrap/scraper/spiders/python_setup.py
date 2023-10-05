import os
import django

# Set the default Django settings module for the 'newScrap' project.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newScrap.settings")

# Set up the Django environment.
if __name__ == "__main__":
    django.setup()
