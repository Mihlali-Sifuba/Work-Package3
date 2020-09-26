import RPi.GPIO as GPIO #Python library used on the Raspberry Pi
import time

GPIO.setmode(GPIO.BOARD) #Set up board GPIO numbering mode
GPIO.setup(11, GPIO.OUT, initial=1) #Set GPIO pin 11 as output and set its initial value to High

#Toggle the LEDs
def main():
    for i in range(0,10):
        GPIO.output(11, True)
        time.sleep(2)
        GPIO.output(11, False)
        time.sleep(2)
    GPIO.cleanup()
    
    
 if __name__ == '__main__':
    main()
