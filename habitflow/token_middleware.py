from django.contrib.sessions.models import Session
from accounts.models import User

class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            session_key = auth_header.split(' ')[1][:32]
            try:
                session = Session.objects.get(session_key=session_key)
                uid = session.get_decoded().get('_auth_user_id')
                if uid:
                    request.user = User.objects.get(pk=uid)
            except Exception:
                pass
        return self.get_response(request)
