import RPi.GPIO as GPIO #Python library used on the Raspberry Pi
import time

GPIO.setmode(GPIO.BOARD) #Set up board GPIO numbering mode
GPIO.setup(11, GPIO.OUT, initial=1) #Set GPIO pin 11 as output and set its initial value to High
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 13 to be an input pin and set initial value to be pulled HIGH
GPIO.setup(15, GPIO.OUT, initial=0) #Set GPIO pin 15 as output and set its initial value to low

#Toggle the LEDs
def main():
    for i in range(0,10): #Loop over 10 times
        GPIO.output(11, True)
        time.sleep(1)
        GPIO.output(11, False)
        time.sleep(1)
    
    
if __name__ == "__main__":
    main()
    pressedButton = True
    while pressedButton: # Run forever if button not pressed
        if GPIO.input(13) == GPIO.LOW:
            GPIO.output(15, True)
            time.sleep(5)
            pressedButton = False
    GPIO.cleanup()
#The end
