import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
UP_BTN = 9
DOWN_BTN = 10

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)

GPIO.output(leds, 0)

GPIO.setup(UP_BTN, GPIO.IN)
GPIO.setup(DOWN_BTN, GPIO.IN)

num = 0
sleep_time = 0.2

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(UP_BTN):
        num += 1
        if num > 255:
            num = 0
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(DOWN_BTN):
        num -= 1
        if num < 0:
            num = 0
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)
