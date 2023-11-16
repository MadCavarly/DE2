from machine import ADC, Pin
from machine import I2C
from sh1106 import SH1106_I2C
import time

#OLED SETUP
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)
oled = SH1106_I2C(128, 64, i2c, addr=0x3c, rotate=180)
oled.contrast(50)
oled.text("Using OLED...", x=0, y=0)
oled.show()


def read_soil_moisture(pin):
    # Read analog value from the soil moisture sensor
    moisture_value = pin.read()

    # Map the analog value to a percentage (assuming a range of 0-1023)
    #buraya ince ayar cekicez
    moisture_percentage = ((1100.0-moisture_value) / 1023.0) * 100.0

    return moisture_percentage
    

def main():
    # Define the pin to which the soil moisture sensor is connected
    moisture_sensor_pin = ADC(Pin(34))

    while True:
        # Read soil moisture level
        moisture_level = read_soil_moisture(moisture_sensor_pin)
        
        # Print the moisture level
        print("Soil Moisture: {:.2f}%".format(moisture_level))
        

        # Wait for some time before the next reading
        time.sleep(2)

if __name__ == "__main__":
    main()
