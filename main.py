from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

on = False

while True:
    on = not on
    led.value(1 if on else 0)
    sleep(2)
