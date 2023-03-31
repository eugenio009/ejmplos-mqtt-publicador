import paho.mqtt.client as mqtt

cliente = mqtt.client()
cliente.connect("192.168.0.35",1883)

data = 2

cliente.publish("demo",data)

print("Fin de Programa")