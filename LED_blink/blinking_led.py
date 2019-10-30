import signal
import sys
from time import sleep  # Import the sleep function from the time module

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(
    8, GPIO.OUT, initial=GPIO.LOW
)  # Set pin 8 to be an output pin and set initial value to low (off)


def signal_handler(sig, frame):  # If exit then set output to LOW
    print("You pressed Ctrl+C!")
    GPIO.output(8, GPIO.LOW)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
print("Press Ctrl+C to stop")

while True:  # Run forever
    GPIO.output(8, GPIO.HIGH)  # Turn on
    sleep(1)  # Sleep for 1 second
    GPIO.output(8, GPIO.LOW)  # Turn off
    sleep(1)  # Sleep for 1 second
