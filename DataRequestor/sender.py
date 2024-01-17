import paho.mqtt.client as mqtt
import os

class MQTTSender:
    def __init__(self, broker_address, broker_port, username, password):
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.connect(broker_address, broker_port, 60)

    def publish_data(self, topic, data):
        self.client.publish(topic, data)

# Odczyt zmiennych środowiskowych
#broker_address = os.environ.get("MQTT_BROKER_ADDRESS")
#broker_port = int(os.environ.get("MQTT_BROKER_PORT"))
#username = os.environ.get("MQTT_USERNAME")
#password = os.environ.get("MQTT_PASSWORD")

#do testow
MQTT_BROKER_ADDRESS = "48.101.108.102"
MQTT_BROKER_PORT = "1883"
MQTT_USERNAME = "student"
MQTT_PASSWORD ="sys-wbud"
broker_address = "MQTT_BROKER_ADDRESS"
broker_port = "MQTT_BROKER_PORT"
username = "MQTT_USERNAME"
password = "MQTT_PASSWORD"



# Utworzenie obiektu sender
sender = MQTTSender(broker_address, broker_port, username, password)

# Przykład użycia
DOWYSLANIA = API.get_data()
sender.publish_data(DOWYSLANIA)