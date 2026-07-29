import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("🔵 CONNECT called")
        self.room_group_name = 'dashboard_updates'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(f"🔵 Added to group: {self.channel_name}")
        await self.accept()
        print("🔵 Connection accepted")

    async def disconnect(self, close_code):
        print(f"🔴 DISCONNECT called: {close_code}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_update(self, event):
        print(f"🟢 send_update called with: {event}")
        await self.send(text_data=json.dumps(event['data']))