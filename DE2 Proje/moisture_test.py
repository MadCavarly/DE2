from machine import ADC, Pin
import time

def read_soil_moisture(pin):
    # Read analog value from the soil moisture sensor
    moisture_value = pin.read()

    # Map the analog value to a percentage (assuming a range of 0-1023)
    #buraya ince ayar cekicez
    moisture_percentage = (moisture_value/ 1023.0) * 25.0

    return moisture_percentage
    

def main():
    # Define the pin to which the soil moisture sensor is connected
    moisture_sensor_pin = ADC(Pin(36))

    while True:
        # Read soil moisture level
        moisture_level = read_soil_moisture(moisture_sensor_pin)
        
        # Print the moisture level
        print("Soil Moisture: {:.2f}%".format(moisture_level))
        

        # Wait for some time before the next reading
        time.sleep(2)

if __name__ == "__main__":
    main()
