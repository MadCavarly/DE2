from machine import Pin, Timer
from machine import PWM

def interruption_handler(timer):
    pin_led.value(not pin_led.value())
    
def interruption_handler1(timer):
    pin_led2.value(not pin_led2.value())
    
def interruption_handler2(timer):
    pin_led3.value(not pin_led3.value())
    
class machine.PWM(dest, *, freq, duty_u16, duty_ns)

PWM(pin_led3,freq=10,)
    
    
#create an object for on-board LED
pin_led = Pin(3, mode=Pin.OUT)
pin_led2 = Pin(1, mode=Pin.OUT)
pin_led3 = Pin(25, mode=Pin.OUT)

timer0 = Timer(0) # Between 0-3 for ESP32
timer1=  Timer(1)
timer2=  Timer(2)

timer0.init(mode=Timer.PERIODIC, period=250, callback=interruption_handler)
timer1.init(mode=Timer.PERIODIC, period=500, callback=interruption_handler1)
timer2.init(mode=Timer.PERIODIC, period=750, callback=interruption_handler2)
#timer0.init(mode=Timer.PERIODIC, freq=2, callback=interruption_handler)