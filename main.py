#!/usr/bin/env python3
import requests
import json
from influxdb import InfluxDBClient
from configparser import ConfigParser
#Parse configuration file
parser = ConfigParser()
parser.read('config.ini')
#Database init
client = InfluxDBClient(host=parser.get('influxdb', 'ip'), port=parser.get('influxdb', 'port'))
client.create_database(parser.get('influxdb', 'database'))
client.switch_database(parser.get('influxdb', 'database'))
#Resultat de la requete API
url =('http://'+parser.get('ecodevice', 'ip')+'/api/xdevices.json?cmd=10')
fetched_url = requests.get(url)
request_result = fetched_url.content
result_dict = json.loads(request_result)

#Creation du bodyJson
json_body = [
    {
        "measurement": "INDEX",
        "tags": {
            "host": result_dict['product']
        },
        "fields": {
            "C1": result_dict['INDEX_C1'],
            "C2": result_dict['INDEX_C2']
        }
    }
]
#Envoi vers Influxdb
client.write_points(json_body)
