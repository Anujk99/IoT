# Program:
# Get input from two switches and switch on corresponding LEDs
#
import RPi.GPIO as GPIO
import time

LED1 = 8
LED2 = 12
BTN1 = 32
BTN2 = 36

def gpio_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BTN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
    
def led_on(LED):
    GPIO.output(LED, GPIO.HIGH)

def led_off(LED):
    GPIO.output(LED, GPIO.LOW)

def led_toggle(LED):
    if GPIO.input(LED):
        led_off(LED)
    else:
        led_on(LED)

def press_2_on(LED, BTN):
    btn = GPIO.input(BTN)
    if btn:
        led_off(LED)
    else:
        led_on(LED)

def press_2_toggle(LED, BTN):
    btn = GPIO.input(BTN)
    if not btn:
        led_toggle(LED)

def main():
    gpio_setup()
    while True:
        press_2_on(LED1, BTN1)
        press_2_toggle(LED2, BTN2)


try:
    main()
finally:
    GPIO.cleanup()
    print("closed Event")
