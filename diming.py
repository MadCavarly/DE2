from machine import Pin, Timer
from machine import PWM
import time

led3=25
led2=1
led1=3
pwm_led1=PWM(Pin(led1,mode=Pin.OUT))
pwm_led2=PWM(Pin(led2,mode=Pin.OUT))
pwm_led3=PWM(Pin(led3,mode=Pin.OUT))

pwm_led1.freq(100)
pwm_led2.freq(500)
pwm_led3.freq(1000)


while True:
    for duty in range(0,1024,5):
        pwm_led1.duty(duty)
        pwm_led2.duty(duty)
        pwm_led3.duty(duty)
        time.sleep_ms(5)
    for duty in range(1023,-1,-5):
        pwm_led1.duty(duty)
        pwm_led2.duty(duty)
        pwm_led3.duty(duty)
        time.sleep_ms(5)
   