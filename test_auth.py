import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "habitflow.settings")
django.setup()

from accounts.models import User
from django.contrib.auth import login
from django.http import HttpRequest
from importlib import import_module
from django.conf import settings

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
request = HttpRequest()
request.session = SessionStore()

# Create a test user
user, created = User.objects.get_or_create(email='test_auth@test.com')
if created:
    user.set_password('testpassword123')
    user.save()

request.user = user
login(request, user)
request.session.save()

print("---")
print("TEST_SESSION_KEY:" + request.session.session_key)
print("---")
