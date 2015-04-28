from nanpy import DHT, SerialManager

import json
import requests

server_url = 'http://localhost:8000'
connection = SerialManager(device='/dev/cu.usbmodem1411')

pins_id = {
    1: DHT(6, DHT.DHT11, connection=connection),
    2: DHT(7, DHT.DHT11, connection=connection),
    3: DHT(8, DHT.DHT11, connection=connection),
}

while True:
    for device_id, dht in pins_id.iteritems():
        headers = {'Content-type': 'application/json'}
        data = {
            'temperature': dht.readTemperature(False),
            'humidity': dht.readHumidity(),
        }
        requests.patch(
            '{0}/devices/{1}/'.format(server_url, device_id),
            data=json.dumps(data),
            headers=headers
        )