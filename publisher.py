import paho.mqtt.client as mqtt

MQTT_HOST = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "SampleTopic"
MQTT_MSG = "Hello MQTT"

def on_connect(mosq,obj,rc):
	print "Connected to MQQT Broker"
	
def on_publish(client,userdata,mid):
	print "Message Published...."
	
mqttc = mqtt.Client()

mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

mqttc.connect(MQTT_HOST,MQTT_PORT,MQTT_KEEPALIVE_INTERVAL)

mqttc.publish(MQTT_TOPIC,MQTT_MSG)

mqttc.disconnect()