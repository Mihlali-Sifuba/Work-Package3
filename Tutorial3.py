import RPi.GPIO as GPIO #Python library used on the Raspberry Pi
import time

GPIO.setmode(GPIO.BOARD) #Set up board GPIO numbering mode
GPIO.output(7, GPIO.OUT) #Set GPIO pin 7 as output

#Toggle the LEDs
for i in range(0,10):
    GPIO.output(11, True)
    time.sleep(0.5)
    GPIO.output(11, False)
GPIO.cleanup()
