# Flash an LED based on cron output (acts as an alarm)


# alarm.py
# act as alarm for cron
import RPi.GPIO as GPIO
from time import sleep

ALARM = 10

def led_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ALARM, GPIO.OUT, initial=GPIO.LOW)

def main():
    led_setup()
	GPIO.output(ALARM, GPIO.HIGH)
	sleep(60)

if __name__=="__main__":
    try:
        main()
    finally:
        GPIO.cleanup()
        print("Closed Everything. END")



# flashing LED as response to alarm
# flash_led.py

import RPi.GPIO as GPIO
from time import sleep

LED = 10

def led_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

def main():
    led_setup()
	alarm = GPIO.input(10)
    while alarm:
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

############ CONSOLE ##################
# $ crontab -e  
# 15 03 * * * python /home/pi/Lab10/alarm.py
# $ python flash_led.py



