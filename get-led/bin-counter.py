import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)

up = 12
down = 19

GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

try:
    while True:
        if GPIO.input(up) == 1:
            num = num + 1
            if num > 255:
                num = 0
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        
        if GPIO.input(down) == 1:
            num = num - 1
            if num < 0:
                num = 255
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        
        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()