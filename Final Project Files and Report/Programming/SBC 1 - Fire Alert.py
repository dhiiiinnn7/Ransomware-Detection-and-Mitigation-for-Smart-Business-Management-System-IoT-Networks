# Import specific functions from the GPIO module to interact with the hardware pins
from gpio import pinMode, digitalRead, customWrite, INPUT, OUTPUT
# Import the time and sleep function from the time module to add delays in the program
from time import time, sleep

# Define constants for the GPIO pin numbers for better readability and maintainability
input_pin = 0  # The pin number for the fire sensor input
sprinkler_pin = 1  # The pin to control the sprinkler system
door_pin = 2  # The pin to control the door (assumed to be a binary open/close system)
window_pin = 3  # The pin to control the window
lcd_pin = 4  # The pin connected to an LCD display for status messages
siren_pin = 5  # The pin to control the siren
fire_detected_value = 1023  # The sensor value indicating fire detection


def fire_alert_system():
    # Set up the GPIO pins with the appropriate input or output designation
    pinMode(input_pin, INPUT)  # Set the fire sensor pin as input
    pinMode(sprinkler_pin, OUTPUT)  # Set the sprinkler control pin as output
    pinMode(door_pin, OUTPUT)  # Set the door control pin as output
    pinMode(window_pin, OUTPUT)  # Set the window control pin as output
    pinMode(lcd_pin, OUTPUT)  # Set the LCD display pin as output
    pinMode(siren_pin, OUTPUT)  # Set the siren control pin as output

    # Print a starting message to indicate that the fire alert system is now running
    print("FIRE ALERT SYSTEM")
    consecutive_no_fire_count = 0  # Initialize a counter to track the number of consecutive no-fire readings

    # Enter an infinite loop to continuously check the fire sensor
    while True:
        fire_value = digitalRead(input_pin)  # Read the value from the fire sensor

        # Check if the sensor value corresponds to the defined fire detection value
        if fire_value == fire_detected_value:
            handle_fire_detected()  # Call a function to handle fire detection actions
            consecutive_no_fire_count = 0  # Reset the no-fire count upon fire detection
        else:
            # If no fire is detected, increment the counter and call the no-fire handler
            consecutive_no_fire_count += 1  # Increment the no-fire count
            print("Consecutive no-fire count: {}".format(
                consecutive_no_fire_count))  # Print the count for logging purposes
            handle_no_fire()  # Call a function to handle the no-fire actions

        # If the system detects no fire for 10 consecutive readings, exit the loop
        if consecutive_no_fire_count >= 10:
            print("No fire detected for 10 consecutive iterations - Exiting loop")
            break  # Break out of the loop to stop the system

        sleep(1)  # Wait for 1 second before the next loop iteration to reduce CPU usage


# Define the function to handle actions when fire is detected
def handle_fire_detected():
    print("FIRE DETECTED")  # Print a message indicating fire detection
    customWrite(sprinkler_pin, '1')  # Activate the sprinkler system
    customWrite(door_pin, '1,0')  # Open the doors
    customWrite(window_pin, '1')  # Open the windows
    customWrite(lcd_pin, 'FIRE DETECTED')  # Update the LCD display with the fire detection message
    customWrite(siren_pin, '1')  # Activate the siren

    # Begin the evacuation announcement procedure when a fire is detected
    last_announcement_time = time()  # Store the initial time when the announcement loop starts
    while True:  # Start an infinite loop to keep announcing until the fire is no longer detected
        current_time = time()  # Get the current time during each iteration of the loop

        # Check if 5 seconds have passed since the last announcement
        if current_time - last_announcement_time >= 5:
            # Print the evacuation message to the console, which would be equivalent to broadcasting the announcement in a real system
            print("Attention please: This is an automated safety notification. "
                  "A fire incident has been detected in the building. "
                  "Please evacuate immediately through the nearest fire exit. "
                  "Do not use elevators. Repeat, do not use elevators. "
                  "Proceed calmly to the closest emergency exit and leave the building. "
                  "Thank you for your cooperation.")

            # Update the last announcement time to the current time after the announcement
            last_announcement_time = current_time

        # Check if the fire is still detected
        if digitalRead(input_pin) != fire_detected_value:
            break  # Exit the while loop if no fire is detected, which ends the evacuation announcements
        sleep(0.1)  # A short sleep to prevent this loop from hogging CPU


# Define the function to handle actions when no fire is detected
def handle_no_fire():
    customWrite(sprinkler_pin, '0')  # Deactivate the sprinkler system
    customWrite(door_pin, '0,1')  # Close the doors
    customWrite(window_pin, '0')  # Close the windows
    customWrite(lcd_pin, 'ALL IS WELL')  # Update the LCD display with an all-clear message
    customWrite(siren_pin, '0')  # Deactivate the siren


# Main entry point of the script
if __name__ == '__main__':
    fire_alert_system()  # Call the fire alert system function to start the system
