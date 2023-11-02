from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C
import time

# I2C(id, scl, sda, freq)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

SENSOR_ADDR = 0x5c
SENSOR_HUMI_REG = 0
SENSOR_TEMP_REG = 2
SENSOR_CHECKSUM = 4

# SH1106_I2C(width, height, i2c, addr, rotate)
display = SH1106_I2C(128, 64, i2c, addr=0x3c, rotate=180)
display.contrast(50)  # Set contrast to 50 %

# https://docs.micropython.org/en/latest/esp8266/tutorial/ssd0306.html


display.show()


print("Stop the code execution by pressing `Ctrl+C` key.")
print("")
print("Scanning I2C... ", end="")
addrs = i2c.scan()
if SENSOR_ADDR in addrs:
    print(f"{hex(SENSOR_ADDR)} detected")
else:
    print("[ERROR] Sensor is not detected")

try:
    while True:
        # readfrom_mem(addr, memaddr, nbytes)
        val = i2c.readfrom_mem(SENSOR_ADDR, SENSOR_HUMI_REG, 4)
        display.fill(color=0)
        
        strg=str(val[2])+"."+str(val[3])+ "C"+ " "+ str(val[0])+"."+str(val[1])+ "%" 
        display.text(strg, x=10, y=25)
        display.show()
        time.sleep(5)

except KeyboardInterrupt:
    print("Ctrl+C Pressed. Exiting...")
