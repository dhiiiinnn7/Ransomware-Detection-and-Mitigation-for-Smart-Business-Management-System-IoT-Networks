# Import various modules needed for the simulation and control of the RFID reader and email notifications
from options import Options
from time import sleep
from physical import *
from gpio import *
from ioeclient import IoEClient
from email import *  # Assume EmailClient is defined elsewhere as shown earlier

# Set constants for the delay between loops and the read distances for the RFID reader
delay_time = 1  # Delay time in seconds
x_read_distance = 50
y_read_distance = 50

# Initialize variables to store the current and last read card IDs, and the current state of the reader
cardID = 0
lastCardID = 0
state = 2  # waiting

# Define an authorized card ID for access control
AUTHORIZED_CARD_ID = 1001

# The setup function configures the IoE (Internet of Everything) client for the RFID reader
def setup():
    IoEClient.setup({
        "type": "RFID Reader",
        "states": [
            {"name": "Card ID", "type": "number", "unit": '', "controllable": False},
            {"name": "Status", "type": "options", "options": {"0": "Valid", "1": "Invalid", "2": "Waiting"}, "controllable": True}
        ]
    })
    # Set up a callback to process data when it is received by the IoE client
    IoEClient.onInputReceive(lambda rinput: processData(rinput, True))
    # Configure the EmailClient with the credentials for sending emails
    EmailClient.setup("iot@networksecurity.com", "networksecurity.com", "IoT", "iOt123!")

# The loop function is the main execution loop of the RFID reader
def loop():
    global cardID, lastCardID, state  # Declare globals to modify them within the function
    # Scan for devices within the specified range
    devices = devicesAt(getCenterX(), getCenterY(), x_read_distance, y_read_distance)
    found = False  # A flag to check if a valid card is found
    for device in devices:
        if device == getName():  # Skip if the detected device is the reader itself
            continue

        # Try to get the card ID property from the detected device
        tempCardID = getDeviceProperty(device, 'CardID')
        if tempCardID:
            try:
                tempCardID = int(tempCardID)  # Convert to an integer
                cardID = tempCardID  # Set the card ID
                found = True  # Mark that we've found a card
                break
            except ValueError:
                continue  # Ignore the device if the card ID is not an integer

    # If no valid card is found, reset the card ID and set the reader's state to waiting
    if not found:
        cardID = lastCardID = 0
        setState(2)
    else:
        # If a new card ID is read that is different from the last, process it
        if lastCardID != cardID:
            lastCardID = cardID
            if cardID == AUTHORIZED_CARD_ID:
                # If the card is authorized, set the state to valid and print a message
                setState(0)
                print("Mr. John with card ID {} has been granted access to the IT server room.".format(cardID))
                # Send an email notification for authorized access
                EmailClient.send("it@networksecurity.com", "Authorized Access", "Mr. John with card ID {} has been granted access to the IT server room.".format(cardID))
            else:
                # If the card is not authorized, set the state to invalid and print a message
                setState(1)
                print("Unauthorized access attempt detected with card ID {}.".format(cardID))
                # Send an email alert for unauthorized access
                EmailClient.send("it@networksecurity.com", "Security Alert", "Unauthorized access attempt detected with card ID {}.".format(cardID))
            # Send a status report
            sendReport()

    # Wait for the specified delay time before running the loop again
    sleep(delay_time)

# Set the state of the RFID reader and write the state to an analog pin (for physical simulation)
def setState(newState):
    global state
    if state != newState:
        state = newState
        analogWrite(A1, state)
        sendReport()

# Send a report of the current state and card ID to the IoE server
def sendReport():
    report = str(cardID) + "," + str(state)
    IoEClient.reportStates(report)

# Process data received from the IoE server
def processData(data, bIsRemote):
    if not data:
        return
    # Split the received data into parts and try to set the state
    data = data.split(",")
    if len(data) > 1:
        try:
            newState = int(data[1])
            setState(newState)
        except ValueError:
            pass  # Ignore if the data cannot be converted to an integer

# Execute the setup function and then run the loop indefinitely
if __name__ == "__main__":
    setup()
    while True:
        loop()
