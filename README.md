<h1>Script to insert ecodevice metrics into InfluxdB</h1>

1. Clone project
```bash
cd /home
git clone https://github.com/martindewaele/ecodevice-influxdb.git
```

2. Install Requirements
```bash
cd /ecodevice-influxdb
pip3 install -r requirements.txt
```
3. Configure config.ini file with the correct values
```python
[influxdb]
ip = localhost --> if the InfluxDB is running on the localserver
port = 8806    --> Default InfluxDB port
database = grafana --> Database name
[ecodevice]
ip = 192.168.253.10 --> IP address of Eco-Device
```
