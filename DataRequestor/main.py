from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "65a2730b52806bec0706fd72c639ceeca86934331a2309edcb8c4de84c66acd1"})

#https://docs.openaq.org/docs/getting-started



url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city=Wroc%C5%82aw&order_by=lastUpdated&dump_raw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

while (True):
    print('Test')
   
    sleep(2)



