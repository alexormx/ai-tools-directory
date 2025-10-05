from django.contrib.auth import login, get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class AutoAdminLoginMiddleware(MiddlewareMixin):  # pragma: no cover (solo dev)
    """Middleware para entornos de desarrollo que evita el formulario de login.

    Activar con DISABLE_ADMIN_AUTH=1 y DJANGO_DEBUG=1. Si no existe un usuario admin,
    se crea uno temporal con password inseguro.
    """
    def process_request(self, request):
        if request.path.startswith('/admin/'):
            if request.user and not isinstance(request.user, AnonymousUser) and request.user.is_authenticated:
                return None
            User = get_user_model()
            user = User.objects.filter(is_superuser=True).first()
            if not user:
                user = User.objects.create_superuser('devadmin', 'devadmin@example.com', 'devpassword123')
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        return None
