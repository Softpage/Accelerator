import paho.mqtt.client as mqtt

MQTT_HOST = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "SampleTopic"

def on_connect(mosq,obj,rc):
    mqttc.subscribe(MQTT_TOPIC,0)
	
def on_subscribe(mosq,obj,mid,granted_qos):
    print "Subscribed to MQTT Topic"
	
def on_message(mosq,obj,msg):
    print msg.payload
	
mqttc=mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_HOST,MQTT_PORT,MQTT_KEEPALIVE_INTERVAL)

mqttc.loop_forever()