# mail_integration/serializers.py
from rest_framework import serializers
from .models import EmailMessage

class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = ['id', 'subject', 'sent_date', 'received_date', 'body', 'attachments']
