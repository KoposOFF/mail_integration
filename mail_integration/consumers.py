# mail_integration/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmailMessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']

        if action == 'fetch_emails':
            # Здесь вызови функцию для получения сообщений и отправь обновления
            # Например:
            # fetch_emails(username, password, server)
            pass

        # Отправка данных клиенту
        await self.send(text_data=json.dumps({
            'message': 'Data sent'
        }))
