import random
from paho.mqtt import client as mqtt_client
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
broker = 'broker.emqx.io'
port = 1883
topic = "/pyside/mqtt"
# generate client ID with pub prefix randomly
#client_id = f'python-mqtt-{random.randint(0, 100)}'

class Sub:

    def __init__(self):
        self.msg = 'None'

    @staticmethod
    def connect_mqtt():
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        client = mqtt_client.Client()
        client.on_connect = on_connect
        client.connect(broker, port)
        return client
    def subscribe(self,client: mqtt_client):
        def on_message(client, userdata, msg):
            msg = f'{msg.payload.decode()}'
            self.msg = msg
        client.subscribe(topic)
        client.on_message = on_message

    def run(self):
        client = self.connect_mqtt()
        self.subscribe(client)
        # msg = self.subscribe(client)
        # self.mysignal.emit(msg)
        client.loop_forever()

if __name__ == '__main__':
    sub = Sub()
    sub.run()