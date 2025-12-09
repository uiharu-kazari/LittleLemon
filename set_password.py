import os
import django
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")
django.setup()

user = User.objects.get(username="admin")
user.set_password("AdminPass2025")
user.save()
print("Password set to: AdminPass2025")
