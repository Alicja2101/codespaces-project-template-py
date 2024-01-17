import paho.mqtt.client as mqtt
import os

class MQTTSubscriber:
    def __init__(self, broker_address, broker_port, username, password):
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.on_message = self.on_message
        self.client.connect(broker_address, broker_port, 60)

    def on_message(self, client, userdata, msg):
        # Przetwarzanie odebranych danych (zapis do pliku, etc.)
        file_name = f"{msg.topic.replace('/', '-')}.txt"
        with open(file_name, "a") as file:
            file.write(msg.payload.decode() + "\n")

    def subscribe(self, topic):
        self.client.subscribe(topic)
        self.client.loop_start()

# Odczyt zmiennych środowiskowych
#broker_address = os.environ.get("MQTT_BROKER_ADDRESS")
#broker_port = int(os.environ.get("MQTT_BROKER_PORT"))
#username = os.environ.get("MQTT_USERNAME")
#password = os.environ.get("MQTT_PASSWORD")

MQTT_BROKER_ADDRESS = "48.101.108.102"
MQTT_BROKER_PORT = "1883"
MQTT_USERNAME = "student"
MQTT_PASSWORD ="sys-wbud"
broker_address = "MQTT_BROKER_ADDRESS"
broker_port = "MQTT_BROKER_PORT"
username = "MQTT_USERNAME"
password = "MQTT_PASSWORD"


# Utworzenie obiektu subscriber
subscriber = MQTTSubscriber(broker_address, broker_port, username, password)
# Subskrypcja dla konkretnego topicu
subscriber.subscribe("#")  # Użyj wildcard "#", aby subskrybować wszystkie topiki