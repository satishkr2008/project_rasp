#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, True)

time.sleep(10)

GPIO.output(23, False)

GPIO.cleanup()

