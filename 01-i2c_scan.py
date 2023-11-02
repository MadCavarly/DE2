from machine import I2C
from machine import Pin

# I2C(id, scl, sda, freq)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

print("Scanning I2C... ", end="")
addrs = i2c.scan()
print(f"{len(addrs)} device(s) detected")

for x in addrs:
    print(f"{x}\t{hex(x)}")