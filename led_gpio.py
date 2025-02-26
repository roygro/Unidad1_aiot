from machine import Pin
import network
import time
from umqtt.simple import MQTTClient

# Configuración de la red WiFi de la Raspberry Pi
SSID = "LOREDO LAP"
PASSWORD = "u55/5B85"
BROKER = "192.168.137.202"
TOPIC = "led/control"

# Conectar a la red WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(1)
print("Conectado a WiFi")

# Configuración del LED en el pin 2
led = Pin(2, Pin.OUT)

def callback(topic, msg):
    print(f"Mensaje recibido: {msg}")
    if msg == b"ON":
        led.value(1)
    elif msg == b"OFF":
        led.value(0)

# Configurar MQTT
client = MQTTClient("ESP32", BROKER)
client.set_callback(callback)
client.connect()
client.subscribe(TOPIC)
print("Conectado al broker MQTT y suscrito al tema")

try:
    while True:
        client.check_msg()
        time.sleep(1)
except KeyboardInterrupt:
    print("Desconectando...")
    client.disconnect()
