import RPi.GPIO as GPIO
import time

led = 26
photo_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo_pin, GPIO.IN)

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0
