import base64

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps

from django.conf import settings

from .models import Key


def accepts_valet_key(func):
    """Enable a view to accept a valet key via HTTP Basic Auth.

    Key ID expected as username, secret as password. On successful auth, the
    request will be set with the valet_key and the user owning the key"""

    @wraps(func)
    def process(request, *args, **kwargs):
        request.valet_key = None
        http_auth = request.META.get('HTTP_AUTHORIZATION', '')
        if http_auth:
            try:
                basic, b64_auth = http_auth.split(' ', 1)
                if 'Basic' == basic:
                    auth = base64.decodestring(b64_auth)
                    key_id, secret = auth.split(':', 1)
                    key = Key.objects.get(key=key_id)
                    if not key.is_disabled and key.check_secret(secret):
                        request.valet_key = key
                        request.user = key.user
            except:
                pass
        return func(request, *args, **kwargs)

    return process
