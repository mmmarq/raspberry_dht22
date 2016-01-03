#!/usr/bin/env python

# Program : Raspberry 2 and DHT22 sensor
# Author : Arduino e Cia

# Load libraries
import Adafruit_DHT
import RPi.GPIO as GPIO

# Set sensor type
sensor = Adafruit_DHT.DHT22

GPIO.setmode(GPIO.BOARD)

# Set GPIO port connected to sensor
pin_sensor = 12

# Read data from sensor
umid, temp = Adafruit_DHT.read_retry(sensor, pin_sensor);

# Show data if read was succesful
if umid is not None and temp is not None:
  print ("Temperature = {0:0.1f}  Humidity = {1:0.1f}\n").format(temp, umid);
else:
  # Show error message if read was not ok
  print("Failed to read sensor data !!!")
