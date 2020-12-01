import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #Sets the way I refer to pins
GPIO.setwarnings(False) #disables this ugly warning

pins=[17,18] #makes list with the pins I use in it
GPIO.setup(pins, GPIO.OUT) #Set pins as output

for i in range(10): #loop 10 times
	GPIO.output(pins, GPIO.HIGH) #on
	sleep(0.5) #wait .5 secs
	GPIO.output(pins, GPIO.LOW) #off
	sleep(0.5)
