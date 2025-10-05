import os
from django.contrib.auth import login, get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class AutoAdminLoginMiddleware(MiddlewareMixin):  # pragma: no cover (solo dev)
    """Middleware para entornos de desarrollo que evita el formulario de login.

    Activar con DISABLE_ADMIN_AUTH=1 y DJANGO_DEBUG=1.

    Política revisada:
    - No se crean usuarios con credenciales hardcodeadas en el repositorio.
    - Si ya existe un superusuario, se reutiliza.
    - (Opcional) Crear superusuario automáticamente sólo si CREATE_DEV_SUPERUSER=1 y
      se proporcionan en .env: DEV_SUPERUSER_NAME, DEV_SUPERUSER_EMAIL, DEV_SUPERUSER_PASSWORD.
    - Si no existe y no se permite creación automática, se omite auto-login (mostrar login normal).
    """
    def process_request(self, request):
        if request.path.startswith('/admin/'):
            if request.user and not isinstance(request.user, AnonymousUser) and request.user.is_authenticated:
                return None
            User = get_user_model()
            user = User.objects.filter(is_superuser=True).first()
            if not user:
                if os.getenv('CREATE_DEV_SUPERUSER', '0') == '1':
                    name = os.getenv('DEV_SUPERUSER_NAME', 'devadmin')
                    email = os.getenv('DEV_SUPERUSER_EMAIL', 'devadmin@example.com')
                    password = os.getenv('DEV_SUPERUSER_PASSWORD', 'ChangeThis!')
                    user = User.objects.create_superuser(name, email, password)
                else:
                    # Sin superuser y sin permiso de creación, no hacemos auto-login
                    return None
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        return None
