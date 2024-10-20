import paho.mqtt.client as mqtt
import time

### callback to be executed whenever we receive a message ###
def on_message(client, userdata, message):
	print("message received", str(message.payload.decode("utf-8")))
	print("message topic= ", message.topic)
	print("message qos= ", message.qos)
	print("message retain flag= ", message.retain)
#############################################################

broker_address = "mqtt.eclipseprojects.io"

topic = "temperature"

print("creating new instance")
client = mqtt.Client("sub")
client.on_message=on_message

print("connecting to broker")
client.connect(broker_address)
client.loop_start()

print("subscribing to topic ", topic)
client.subscribe(topic)

time.sleep(30)

client.loop_stop()
