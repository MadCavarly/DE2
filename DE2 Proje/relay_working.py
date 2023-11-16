from machine import Pin
import time

pin_relay = Pin(3, mode=Pin.OUT)

while True:
    pin_relay.on()
    time.sleep_ms(200)
    pin_relay.off()
    time.sleep_ms(2000)