
import requests
import time
import os
import json
import paho.mqtt.client as mqtt



# class MQTTSubscriber:
#     def __init__(self, broker_address, broker_port, username, password):
#         self.client = mqtt.Client()
#         self.client.username_pw_set(username, password)
#         self.client.connect(broker_address, broker_port, 60)


# class MQTTSender:
#     def __init__(self, broker_address, broker_port, username, password):
#         self.client = mqtt.Client()
#         self.client.username_pw_set(username, password)
#         self.client.connect(broker_address, broker_port, 60)


# broker_address = os.environ.get("MQTT_BROKER_ADDRESS")
# broker_port = int(os.environ.get("MQTT_BROKER_PORT"))
# username = os.environ.get("MQTT_USERNAME")
# password = os.environ.get("MQTT_PASSWORD")

#subscriber = MQTTSubscriber(broker_address, broker_port, username, password)
#sender = MQTTSender(broker_address, broker_port, username, password)



res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "65a2730b52806bec0706fd72c639ceeca86934331a2309edcb8c4de84c66acd1"})

#https://docs.openaq.org/docs/getting-started



url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city=Wroc%C5%82aw&order_by=lastUpdated&dump_raw=false" 
#url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&city=Sopot&order_by=lastUpdated&dump_raw=false"


headers = {"accept": "application/json"}

response = requests.get(url, headers=headers).json()


##########################zeby konsola wyplula ladny kod
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=5)
    print(text)
##########################
#jprint(response.json())


class WeatherRequester:
    def __init__(self, city): #metody, city - artybuty
        self.city = city
        

    def get_data(self):
        data = {
        "Dane dla" : self.city,
        "Lokacja z pobieranych danych": (response["results"][0]["city"]),
        "Czas pobrania danych":response["results"][0]["parameters"][0]["lastUpdated"],
        "Aktualna jakosc powietrza": (response["results"][0]["parameters"][0]["lastValue"], response["results"][0]["parameters"][0]["unit"])
        }
        
        return(data)
        #print(f"Lokacja z pobieranych danych {self.location}, Czas pobrania danych {self.timestamp} Aktualna jakosc powietrza {self.value} µg/m³")
    

#print(response.text)


#tworzenie
DANE_API = WeatherRequester(os.getenv('MIASTO')) 
#API = WeatherRequester('Wrocław') #pokazowe w konsoli

while (True):
   
 
   
   #jprint(API.get_data())
    print(DANE_API.get_data())
    
    time.sleep(10)
