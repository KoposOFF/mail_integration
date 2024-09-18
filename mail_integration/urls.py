# mail_integration/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailMessageViewSet
from . import views

router = DefaultRouter()
router.register(r'messages', EmailMessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('messages/', views.message_list, name='message_list'),
]
