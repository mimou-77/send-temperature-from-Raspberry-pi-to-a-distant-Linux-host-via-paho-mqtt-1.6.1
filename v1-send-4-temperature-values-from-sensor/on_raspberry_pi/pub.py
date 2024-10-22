import paho.mqtt.client as mqtt 
import time

broker_address = "mqtt.eclipseprojects.io"

topic = "temperature"

#### callback that executes whenever we send a message ###
def on_publish(client, userdata, message):
	print("msg sent")
##########################################################

print("creating new instance")
client = mqtt.Client("pub")

client.on_publish=on_publish

print("connecting to broker")
client.connect(broker_address)

client.loop_start()

print("publishing msg to topic ", topic)
client.publish(topic, "27")

time.sleep(4)

print("publishing msg  to topic ", topic)
client.publish(topic, "23")

time.sleep(4)

print("publishing msg to topic ", topic)
client.publish(topic, "7")

time.sleep(4)

client.loop_stop()
