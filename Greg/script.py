
import json
from influxdb import InfluxDBClient
#Configure InfluxDB Database
client = InfluxDBClient(host='localhost', port=8086)
client.create_database('nombril')
client.switch_database('nombril')

#Resultat de la requete API
request_result = '{"product":"Eco-devices","T1_PTEC":"----","T1_PAPP":0,"T1_BASE":0,"T2_PTEC":"----","T2_PAPP":0,"T2_BASE":0,"INDEX_C1":287000,"INDEX_C2":1436.965}'
result_dict = json.loads(request_result)

#Variabilisation des donnees
product = result_dict['product']
index_c1 = result_dict['INDEX_C1']
index_c2 = result_dict['INDEX_C2']

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

