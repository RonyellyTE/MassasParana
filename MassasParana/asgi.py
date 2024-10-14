"""
ASGI config for MassasParana project.

It exposes the ASGI callable as a module-level variable named ``application``.

asgi.py:
Descrição: Configura o servidor ASGI (Asynchronous Server Gateway Interface) para aplicações assíncronas. Útil para projetos que utilizam funcionalidades assíncronas.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MassasParana.settings')

application = get_asgi_application()
