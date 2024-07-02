from gpio import *
from time import *

# Constants for the GPIO pin numbers and motion detected value
motion_sensor_pin = 6
camera_pin = 7
door_pin = 8
light_pin = 9
motion_detector_value = 1023  # The value indicating motion is detected

def setup_pins():
    """Set up GPIO pins as input or output as required."""
    pinMode(motion_sensor_pin, INPUT)
    pinMode(camera_pin, OUTPUT)
    pinMode(door_pin, OUTPUT)
    pinMode(light_pin, OUTPUT)

def motion_detected_actions():
    """Actions to perform when motion is detected."""
    customWrite(camera_pin, '1')  # Activate Camera
    customWrite(door_pin, '1,0')  # Unlock/Open Door
    customWrite(light_pin, '2')  # Turn on Light
    print("Actions executed: Camera activated, Door opened, Light turned on.")

def no_motion_actions():
    """Actions to perform when no motion is detected."""
    customWrite(camera_pin, '0')  # Deactivate Camera
    customWrite(door_pin, '0,0')  # Lock/Close Door
    customWrite(light_pin, '0')  # Turn off Light
    print("Actions executed: Camera deactivated, Door closed, Light turned off.")

def main():
    print("Starting SMART DOOR SYSTEM BY MOTION SENSOR")
    setup_pins()

    no_motion_count = 0  # Initialize counter for consecutive no-motion readings

    while True:
        if digitalRead(motion_sensor_pin) == motion_detector_value:
            print("Security Alert: Motion has been detected near the reception hall. "
      			  "An individual may be approaching. Please verify their identification immediately.")
            no_motion_count = 0  # Reset the no-motion counter
            motion_detected_actions()
        else:
            no_motion_count += 1
            print("No motion detected. Count: {}".format(no_motion_count))
            no_motion_actions()

            # Exit the loop if no motion is detected for a predefined number of times
            if no_motion_count >= 10:
                print("No motion detected for 10 consecutive checks - Exiting system.")
                break

        sleep(1)  # Wait for 1 second before checking again

if __name__ == '__main__':
    main()from gpio import *
from time import *

# Constants for the GPIO pin numbers and motion detected value
motion_sensor_pin = 6
camera_pin = 7
door_pin = 8
light_pin = 9
motion_detector_value = 1023  # The value indicating motion is detected

def setup_pins():
    """Set up GPIO pins as input or output as required."""
    pinMode(motion_sensor_pin, INPUT)
    pinMode(camera_pin, OUTPUT)
    pinMode(door_pin, OUTPUT)
    pinMode(light_pin, OUTPUT)

def motion_detected_actions():
    """Actions to perform when motion is detected."""
    customWrite(camera_pin, '1')  # Activate Camera
    customWrite(door_pin, '1,0')  # Unlock/Open Door
    customWrite(light_pin, '2')  # Turn on Light
    print("Actions executed: Camera activated, Door opened, Light turned on.")

def no_motion_actions():
    """Actions to perform when no motion is detected."""
    customWrite(camera_pin, '0')  # Deactivate Camera
    customWrite(door_pin, '0,0')  # Lock/Close Door
    customWrite(light_pin, '0')  # Turn off Light
    print("Actions executed: Camera deactivated, Door closed, Light turned off.")

def main():
    print("Starting SMART DOOR SYSTEM BY MOTION SENSOR")
    setup_pins()

    no_motion_count = 0  # Initialize counter for consecutive no-motion readings

    while True:
        if digitalRead(motion_sensor_pin) == motion_detector_value:
            print("Security Alert: Motion has been detected near the reception hall. "
      			  "An individual may be approaching. Please verify their identification immediately.")
            no_motion_count = 0  # Reset the no-motion counter
            motion_detected_actions()
        else:
            no_motion_count += 1
            print("No motion detected. Count: {}".format(no_motion_count))
            no_motion_actions()

            # Exit the loop if no motion is detected for a predefined number of times
            if no_motion_count >= 10:
                print("No motion detected for 10 consecutive checks - Exiting system.")
                break

        sleep(1)  # Wait for 1 second before checking again

if __name__ == '__main__':
    main()