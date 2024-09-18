# mail_integration/views.py
from rest_framework import viewsets
from .models import EmailMessage
from .serializers import EmailMessageSerializer

class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer
