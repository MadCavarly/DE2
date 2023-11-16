from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C
import time

# I2C(id, scl, sda, freq)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

# SH1106_I2C(width, height, i2c, addr, rotate)
oled = SH1106_I2C(128, 64, i2c, addr=0x3c, rotate=180)
oled.contrast(50)  # Set contrast to 50 %

oled.text("UsingnmOLED...", x=0, y=0)

oled.show()

print("Stop the code execution by pressing `Ctrl+C` key.")
print("If it does not respond, press the onboard `reset` button.")

try:
    while True:
        time.sleep(.1)

except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting...")
    oled.poweroff()