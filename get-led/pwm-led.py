import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo_pin, GPIO.IN)

led = 26
photo_pin = 6

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0
