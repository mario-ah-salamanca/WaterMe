
from channels.consumer import SyncConsumer

class SensorConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            'temperature_c': event['temperature_c'],
            'temperature_f': event['temperature_f'],
            'humidity': event['humidity'],
        })


