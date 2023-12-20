from time import sleep
#from snap7.server import mainloop
import requests
import time

res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "65a2730b52806bec0706fd72c639ceeca86934331a2309edcb8c4de84c66acd1"})

#https://docs.openaq.org/docs/getting-started



##
parameters = {
   "city": "city",
   "id": "id"
}


url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city=Wroc%C5%82aw&order_by=lastUpdated&dump_raw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, params=parameters).json()
#response = requests.get(url, headers=headers, params=parameters)
#response = requests.get(url, params=parameters)



#zeby konsola wyplula ladny kod
import json
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



#jprint(response.json())


class WeatherRequester:
    def __init__(self, location, timestamp, values):
        self.location = location
        self.timestamp = timestamp
        self.values = values
    def wyslij_dane(self):
        print(f"Lokacja z pobieranych danych {self.location}, Czas pobrania danych {self.timestamp} Aktualna jakosc powietrza {self.value} µg/m³")

#print(response.text)



#def main():
#dane = WeatherRequester(["results"][0]["name"], 31, 80)  ?????????????




data={
"Lokacja z pobieranych danych": response["results"][0]["name"],
"Czas pobrania danych":response["results"][0]["parameters"][0]["lastUpdated"],
"Aktualna jakosc powietrza":response["results"][0]["parameters"][0]["lastValue"]
}
data_to_send=json.dumps(data)
print(data_to_send)






while (True):
    
   # print('Lokacja z pobieranych danych')
   # print(response["results"][0]["name"])

    ##print('Czas pobrania danych')
    #print(response["results"][0]["parameters"][0]["lastUpdated"])

    #print('Aktualna jakosc powietrza')
   # print(response["results"][0]["parameters"][0]["lastValue"])
    #print(response["results"][0]["parameters"][0]["parameter"])
    
    
    print(data_to_send)


    time.sleep(30)
    sleep(2)



