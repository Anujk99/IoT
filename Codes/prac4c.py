# Program:
# Flash an LED at a given on time and off time cycle, 
# where the two times are taken from a file.
#
import time
import csv
import sys
import RPi.GPIO as GPIO
from time import sleep


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

def read_time():
    timing = []
    with open(sys.argv[1], 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            timing.append((row[0], row[1]))
        return timing[1:]

def main():
    setup()
    time_seq = read_time()
    for on, off in time_seq:
        GPIO.output(10, GPIO.HIGH)
        print("LED ON")
        time.sleep(float(on))
        GPIO.output(10, GPIO.LOW)
        print("LED OFF")
        time.sleep(float(off))

try:
    main()
finally:
    GPIO.cleanup()
    print("END")
