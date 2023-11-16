from machine import I2C
from machine import Pin
import time

# I2C(id, scl, sda, freq)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

SENSOR_ADDR = 0x5c
SENSOR_HUMI_REG = 0
SENSOR_TEMP_REG = 2
SENSOR_CHECKSUM = 4

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
        val = i2c.readfrom_mem(SENSOR_ADDR, SENSOR_HUMI_REG, 5)
        
        print(f"{val[2]}.{val[3]} {chr(176)}C",f"{val[0]}.{val[1]}%  {val[4]}    ")
        time.sleep(5)

except KeyboardInterrupt:
    print("Ctrl+C Pressed. Exiting...")