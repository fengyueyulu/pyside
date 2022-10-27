import random
from paho.mqtt import client as mqtt_client
from PySide2.QtWidgets import *
from PySide2.QtCore import Signal, Slot, QObject

broker = 'broker.emqx.io'
port = 1883
topic = "/pyside/mqtt"
# generate client ID with pub prefix randomly
#client_id = f'python-mqtt-{random.randint(0, 100)}'

class MySignal(QObject):
    check_sub_signal1=Signal(str)
    check_sub_signal2=Signal(float)

@Slot()
def setLCDNumber(num):
    print(num)
    pass

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
my=MySignal()
my.check_sub_signal1.connect(setLCDNumber)
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        # global num_status
        # tmp=[0]
        # if(msg.payload.decode()!="" ):
        #     if(msg.payload.decode()!=tmp[-1]):
        #         my.check_sub_signal1.emit(msg.payload.decode())
        #         print(type(msg.payload.decode()))
        #         tmp.append(msg.payload.decode())
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
