# Intrumento de evaluación
# Asignatura. Aplicaciones IoT
# GDS0653
# Unidad 1
# Total de horas 30 (8 teóricas, 22 prácticas)
# Evaluación Ordinaria 
# Princes Rocio Guerrero Sánchez 
# 1223100399
<br>

## Objetivo general de la unidad
El estudiante manipulará sensores y actuadores conectados a hardware abierto para procesar y almacenar datos, desarrollando habilidades teóricas, prácticas y de integración de sistemas IoT.
<br>
<br>

# Teoria 
## NetAcad Python Fundamentals 2
Link de los examnes: https://drive.google.com/drive/folders/1eu7cSfn7R2gu467BViHtbbsLU_rBC2RY?usp=sharing

<br>

# Practica
## Ejercicio 1. Almacenamiento de Datos y Ejercicio 2: Control de Actuadores
https://drive.google.com/drive/folders/1ePl-27OL2kEvUKwbZN0OTxKv0XK_M3MH?usp=sharing

<code> 

import network
import time
from machine import Pin, time_pulse_us, PWM
from umqtt.simple import MQTTClient

# Configuración Wi-Fi
wifi_ssid = "Wifimax pro"  # Cambia por tu SSID
wifi_password = "Estudiantes2024"  # Cambia por tu contraseña


mqtt_broker = "192.168.1.195"  # IP de tu Raspberry Pi
mqtt_port = 1883 
mqtt_topic = "jjlm/sensor"  # Tema donde se publicarán los datos
mqtt_client_id = "sensor_{}".format(int(time.time()))  # ID único


TRIGGER_PIN = 5
ECHO_PIN = 18

trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


led_red = PWM(Pin(14), freq=1000)  # Pin Rojo
led_green = PWM(Pin(12), freq=1000)  # Pin Verde
led_blue = PWM(Pin(13), freq=1000)  # Pin Azul


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Conectando a la red Wi-Fi...')
        wlan.connect(wifi_ssid, wifi_password)
        
        timeout = 10  # Esperar hasta 10 segundos para la conexión
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1

    if wlan.isconnected():
        print('Conexión Wi-Fi exitosa:', wlan.ifconfig())
    else:
        print("Error: No se pudo conectar a Wi-Fi")
        return False
    return True

def connect_mqtt():
    try:
        client = MQTTClient(mqtt_client_id, mqtt_broker, mqtt_port)
        client.connect()
        print("Conectado al broker MQTT")
        return client
    except Exception as e:
        print("Error al conectar al broker MQTT:", e)
        return None

# Función para medir la distancia con el sensor HC-SR04
def measure_distance():
    trigger.off()
    time.sleep_us(2)
    trigger.on()
    time.sleep_us(10)
    trigger.off()

    pulse_time = time_pulse_us(echo, 1, 30000)  # Tiempo en microsegundos
    if pulse_time < 0:
        return None  # Fallo en la medición

    distance = (pulse_time / 2) * 0.0343  # Conversión a cm
    return round(distance, 2)

# Función para cambiar el color del LED en función de la distancia
def set_led_color(distance):
    if distance is not None:
        # Cambiar colores dependiendo de la distancia
        if distance < 10:
            led_red.duty(1023)  # Rojo
            led_green.duty(0)  # Apagar Verde
            led_blue.duty(0)  # Apagar Azul
        elif 10 <= distance < 20:
            led_red.duty(0)  # Apagar Rojo
            led_green.duty(1023)  # Verde
            led_blue.duty(0)  # Apagar Azul
        elif 20 <= distance < 30:
            led_red.duty(0)  # Apagar Rojo
            led_green.duty(0)  # Apagar Verde
            led_blue.duty(1023)  # Azul
        else:
            led_red.duty(0)  # Apagar Rojo
            led_green.duty(0)  # Apagar Verde
            led_blue.duty(0)  # Apagar Azul
    else:
        # Si no hay medición, apagar LED
        led_red.duty(0)
        led_green.duty(0)
        led_blue.duty(0)

# Enviar datos del sensor por MQTT solo si cambian
def publish_data(client, last_distance):
    if client is None:
        print("MQTT no está conectado")
        return last_distance

    try:
        distance = measure_distance()
        if distance is not None and distance != last_distance:
            payload = "{}".format(distance)
            client.publish(mqtt_topic, payload)
            print("Distancia enviada:", payload, "cm")
            set_led_color(distance)  # Cambiar color del LED
            return distance  # Actualizar el último valor enviado
        else:
            print("Distancia sin cambios, no se envía")
            return last_distance
    except Exception as e:
        print("Error al medir la distancia:", e)
        return last_distance

# Main
if connect_wifi():  # Conectar a Wi-Fi
    client = connect_mqtt()  # Conectar a MQTT
    last_distance = None  # Última distancia medida

    while True:
        last_distance = publish_data(client, last_distance)  # Enviar datos solo si cambia
        time.sleep(2)  # Medir cada 2 segundos
else:
    print("No se pudo establecer conexión Wi-Fi. Reinicia el dispositivo.")

    </code>

<br>
<br>



## Ejercicios 3 (soldadura): Circuito funcional en placa fenólica

<img src="https://drive.google.com/uc?export=view&id=1L4AzfGDi5IXGYXrK-AvPs4vF6VzBZmTA" width="150"/>
<img src="https://drive.google.com/uc?export=view&id=1Dt4lalCZgzDO0QtzSdBGyJ-3q4eMAflH" width="150"/>

<br>

## Ejercicios 4 (soldadura): Figura 2D o 3D soldada

<img src="https://drive.google.com/uc?export=view&id=1V9xVktQPwy9U-pYlTwRwYl1bGNNF_KQH" width="150"/>

<br>

## Ejercicios en clase: Videos demostrativos
https://drive.google.com/drive/folders/1gqua6V7e8ARg5rZH31vTtbZb9p9EKa4u?usp=sharing
<br>
<br>
