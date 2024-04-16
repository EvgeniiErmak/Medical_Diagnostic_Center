# online_consultations/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ConsultationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.consultation_id = self.scope['url_route']['kwargs']['consultation_id']
        self.room_group_name = f'consultation_{self.consultation_id}'

        # Подключение к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Отключение от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Получение сообщений от WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправка сообщения всем участникам группы
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'consultation.message',
                'message': message
            }
        )

    # Получение сообщения от группы
    async def consultation_message(self, event):
        message = event['message']

        # Отправка сообщения WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
