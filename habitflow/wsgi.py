import os
import sys
from pathlib import Path

# Ensure the project root is on the path so Django can find all apps
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habitflow.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()          # Vercel looks for "app"
application = app                     # gunicorn / local looks for "application"

# Run migrations automatically for Vercel deployments
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Auto-migration failed (this is normal locally): {e}")
