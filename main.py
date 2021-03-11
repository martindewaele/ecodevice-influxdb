#import modules
import json
import requests
from influxdb import InfluxDBClient
#configuration InfluxDB
client = InfluxDBClient(host='localhost', port=8086)
client.create_database('grafana')
client.switch_database('grafana')
#GET resultat ecodevice
fetched_url = requests.get('http://192.168.253.102/api/xdevices.json?cmd=10')
request_result = fetched_url.content
result_dict = json.loads(request_result)
#Variabilisation des donnees
product = result_dict['product']
index_c1 = result_dict['INDEX_C1']
index_c2 = result_dict['INDEX_C2']

#Creation du data-set et push vers InfluxDB
json_body = [
    {
        "measurement": "INDEX",
        "tags": {
            "host": product
        },
        "fields": {
            "C1": index_c1,
            "C2": index_c2
        }
    }
]
print(json_body)
client.write_points(json_body)



