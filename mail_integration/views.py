# mail_integration/views.py
from rest_framework import viewsets
from .models import EmailMessage
from .serializers import EmailMessageSerializer
from django.shortcuts import render

class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer

def message_list(request):
    return render(request, 'mail_integration/messages_list.html')