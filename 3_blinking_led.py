from machine import Pin
from time import sleep_ms

# Check the LED pin on your board, usually it is GPIO2
led = Pin(3, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(25, Pin.OUT)


# Forever loop
while True:
    led.on()
    sleep_ms(200)
    led.off()
    led2.on()
    sleep_ms(200)
    led2.off()
    led3.on()
    sleep_ms(200)
    led3.off()