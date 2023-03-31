import paho.mqtt.client as mqtt

cliente = mqtt.Client()
cliente.connect ("192.168.0.35",1883)

data = "Hola"

client.publish("demo",data)

print("Fin de programa")