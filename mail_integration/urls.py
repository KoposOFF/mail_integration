# mail_integration/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailMessageViewSet

router = DefaultRouter()
router.register(r'messages', EmailMessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
