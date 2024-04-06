from machine import Pin, PWM
from time import sleep

led = Pin("LED", Pin.OUT)

motor_speed = PWM(Pin(18, Pin.OUT))
motor_in1 = Pin(17, Pin.OUT)
motor_in2 = Pin(16, Pin.OUT)

motor_in1.high()
motor_in2.low()
motor_speed.freq(22000)
motor_speed.duty_u16(40000)

led_on = False

while True:
    led_on = not led_on
    led.value(1 if led_on else 0)
    sleep(2)
