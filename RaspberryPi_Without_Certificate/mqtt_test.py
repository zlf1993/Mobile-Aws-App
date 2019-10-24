import paho.mqtt.client as mqtt
import json
import sys
from camera import Camera

cafile = "/home/pi/Documents/aws-iot/root-CA.crt"
cerfile = "/home/pi/Documents/aws-iot/26ebf42df6-certificate.pem.crt"
keyfile = "/home/pi/Documents/aws-iot/26ebf42df6-private.pem.key"

SERVER = "a37i47xeh8qin6-ats.iot.us-east-2.amazonaws.com"
PORT = 8883

TOPIC = "my/topic"
QOS = 1

message = {"default":"something"}
Data_Out = json.dumps(message)

def on_connect(client, userdata, flags, rc):
    print("Connect with result code " + str(rc))
    
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    
cam = Camera(384, 192, True)
imgJson = cam.takePicture()
cam.releaseCam()
print(imgJson)
    
client = mqtt.Client(client_id="", clean_session=True, userdata=None, transport="tcp")
client.tls_set(cafile, cerfile, keyfile)
client.on_connect = on_connect
client.on_message = on_message

client.connect(host=SERVER, port=PORT, keepalive=60, bind_address="")
client.loop_start()

client.publish(topic=TOPIC, payload=imgJson, qos=QOS, retain=False)

client.loop_stop()
client.disconnect()


