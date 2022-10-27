import random
import time

from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "/pyside/mqtt"
# generate client ID with pub prefix randomly
#client_id = f'python-mqtt-{random.randint(0, 1000)}'

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

def publish(client):
    msg_count = 0
    times = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    temperature = [30, 32, 24, 31, 19, 12, 20, 28, 38, 30]
    humidity = [10, 12, 13, 9, 3, 14, 17, 12, 11, 10]
    ch4 = [1, 2, 2.4, 1.2, 1.8, 1.3, 2.5, 3.1, 4.6, 3.4]
    while True:
        time.sleep(1)
        try:
            msg1 = f"temperature:{temperature[msg_count]}"
            #print(msg1)
            time.sleep(0.5)
            msg2 = f"humidity:{humidity[msg_count]}"
            #print(msg2)
            time.sleep(0.5)
            msg3 = f"ch4:{ch4[msg_count]}"
            #print(type(msg3))
            time.sleep(0.5)
            result = client.publish(topic, msg1)
            client.publish(topic, msg2)
            client.publish(topic, msg3)

        except:
            break
        result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send`{msg1}` to topic`{topic}`")
            print(type(msg1))
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()