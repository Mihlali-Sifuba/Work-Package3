import RPi.GPIO as GPIO #Python library used on the Raspberry Pi
import time

GPIO.setmode(GPIO.BOARD) #Set up board GPIO numbering mode
GPIO.output(11, GPIO.OUT, initial=1) #Set GPIO pin 11 as output and set its initial value to High

#Toggle the LEDs
for i in range(0,10):
    GPIO.output(11, True)
    time.sleep(0.5)
    GPIO.output(11, False)
GPIO.cleanup()
