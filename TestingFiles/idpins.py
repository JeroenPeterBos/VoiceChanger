import RPi.GPIO as gpio
import time

def pinon(pin):
        gpio.setmode(gpio.BCM)
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, 1)
        time.sleep(1)
        gpio.output(pin, 0)
        gpio.cleanup()
