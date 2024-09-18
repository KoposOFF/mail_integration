# mail_integration/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/messages/$', consumers.EmailMessageConsumer.as_asgi()),
]
