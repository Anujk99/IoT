# Program:
# Light an LED through Python program
#
import RPi.GPIO as GPIO
from time import sleep

LED = 10

def led_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

def main():
    led_setup()
    while True:
        GPIO.output(LED, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED, GPIO.LOW)
        sleep(1)

if __name__=="__main__":
    try:
        main()
    finally:
        GPIO.cleanup()
        print("Closed Everything. END")
