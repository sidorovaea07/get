import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
photo_pin = 6

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(photo_pin, GPIO.IN)
GPIO.output(leds, 0)

light_time = 0.2

for led in leds:
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)

for led in reversed(leds): 
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)   