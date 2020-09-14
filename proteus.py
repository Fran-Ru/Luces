import datetime
import paho.mqtt.client as mqtt 
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup (7, GPIO.OUT)
GPIO.setup (11, GPIO.IN)



def on_message(client, obj, msg):    
	tex =(msg.payload.decode("utf-8"))
	z=True
	print(tex)
	if tex== 'luces' and GPIO.input(11):
		mqttc.publish("saturno101@outlook.com/servidor","Las luces esta encendida")
		z=False
	if tex== 'luces' and z:
		mqttc.publish("saturno101@outlook.com/servidor","Las luces esta apagada")
	if tex=='clave':
		mqttc.publish("saturno101@outlook.com/servidor","La clave por favor")


mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("saturno101@outlook.com","10prmillcoma") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("saturno101@outlook.com/focos", 0)

rc=0
print("Conexion...")
i = 0
while rc == 0:
	time.sleep(2)
	rc = mqttc.loop()
	i =i+1
	if GPIO.input(11) ==True:
	    F =open("texto.txt","w")
	    y=datetime.datetime.now()
	    fecha =str(y)
	    print(fecha)
	    F.write(fecha)
	    F.close()
	    
	if GPIO.input(11):
		GPIO.output(7, True)
	else:
		GPIO.output(7, False)

