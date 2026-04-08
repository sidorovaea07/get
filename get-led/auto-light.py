import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 26
photo_pin = 6

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(photo_pin, GPIO.IN)

while True:
        GPIO.output(led_pin, not GPIO.input(photo_pin))
        time.sleep(0.5)