from django.db import models

class EmailAccount(models.Model):
    service_provider = models.CharField(max_length=255)  # Например, Gmail, Yandex
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.service_provider}: {self.login}"

class EmailMessage(models.Model):
    subject = models.CharField(max_length=255)  # Тема сообщения
    send_date = models.DateTimeField()  # Дата отправки
    received_date = models.DateTimeField()  # Дата получения
    body = models.TextField()  # Текст сообщения
    attachments = models.TextField(blank=True, null=True)  # Список файлов

    account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)  # Аккаунт, с которого получено сообщение

    def __str__(self):
        return f"{self.subject} (Отправлено: {self.send_date})"
