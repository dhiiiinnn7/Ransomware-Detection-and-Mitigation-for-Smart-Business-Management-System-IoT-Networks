# Import specific functions from the GPIO module to interact with the hardware pins
from gpio import *
# Import the time and sleep function from the time module to add delays in the program
from time import time, sleep

# Constants for the GPIO pin numbers and temperature thresholds
temperature_sensor_pin = 0
ac_pin = 3
heater_pin = 2
lcd_pin = 1
temp_high_threshold = 520  # The temperature value that triggers the AC
temp_low_threshold = 510   # The temperature value that triggers the heater

def setup_pins():
    """Initialize GPIO pins."""
    pinMode(temperature_sensor_pin, INPUT)
    pinMode(ac_pin, OUTPUT)
    pinMode(heater_pin, OUTPUT)
    pinMode(lcd_pin, OUTPUT)

def turn_on_ac():
    """Activate the air conditioning system and update the LCD."""
    digitalWrite(ac_pin, HIGH)
    customWrite(lcd_pin, "AC-ON")
    print("Air conditioning activated.")

def turn_on_heater():
    """Activate the heating system and update the LCD."""
    digitalWrite(heater_pin, HIGH)
    customWrite(lcd_pin, "HEATER-ON")
    print("Heating system activated.")

def maintain_normal_temp():
    """Turn off all temperature control systems and update the LCD to indicate normal temperature."""
    digitalWrite(ac_pin, LOW)
    digitalWrite(heater_pin, LOW)
    customWrite(lcd_pin, "NORMAL-TEMP")
    print("Temperature is normal. All systems standby.")

def main():
    print("Starting SMART ROOM TEMPERATURE system")
    setup_pins()

    while True:
        # Read temperature from the sensor
        temp = digitalRead(temperature_sensor_pin)
        print("Temperature Reading: {}".format(temp))

        # Determine and apply temperature control actions
        if temp >= temp_high_threshold:
            turn_on_ac()
        elif temp < temp_low_threshold:
            turn_on_heater()
        else:
            maintain_normal_temp()

        sleep(3)  # Wait for 3 seconds before the next read

if __name__ == "__main__":
    main()