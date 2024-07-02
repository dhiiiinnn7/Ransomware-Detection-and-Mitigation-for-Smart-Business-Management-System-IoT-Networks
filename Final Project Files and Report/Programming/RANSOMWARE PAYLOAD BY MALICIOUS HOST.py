# Import necessary modules for TCP communication and delaying operations
from tcp import *
from time import sleep
from simulation import *

# Define the IP address and port of the IoT device that Malicious Host will connect to
serverIP = "192.168.0.3"
serverPort = 1025
# Define the protocol and PDU type that will be used for sending data
protocolName = "MyProtocol2"
pduType = "Ransomware"
# Define the color that will be used for the PDU for visualization purposes
pduColor = 0xff00ff

# Create a TCPClient instance for managing the TCP connection
client = TCPClient()

# Callback function that's called when the TCP connection state changes
def onTCPConnectionChange(type):
    # Print the new connection state to the console
    print("Connection state changed to {}".format(type))

# Callback function for handling PDU received from the IoT device
def onTCPReceiveWithPDUInfo(data, pduInfo):
    # Print the response data from the IoT device to the console
    print("Response PDU received with data:", data)

# The main function where the Malicious Host's behavior is defined
def main():
    # Register the callback functions with the Malicious Host instance
    client.onConnectionChange(onTCPConnectionChange)
    client.onReceiveWithPDUInfo(onTCPReceiveWithPDUInfo)

    # Attempt to connect to the server using the provided IP address and port
    if client.connect(serverIP, serverPort):
        # If the connection is successful, print a confirmation message
        print("Connected to server.")
    else:
        # If the connection fails, print an error message and exit the function
        print("Failed to connect to server.")
        return

    # Enter an infinite loop where the Malicious Host periodically sends PDUs to the IoT device
    while True:
        # Create a PDUInfo object with the specified color
        pduInfo = PDUInfo(pduColor)
        # Add a message to the PDU
        pduInfo.addOutMessage("Ransomware trigger command")

        # Set the format of the outgoing PDU with the command to trigger ransomware
        pduInfo.setOutFormat(protocolName, pduType, {
            "type": "COMMAND",
            "command": "TRIGGER_RANSOMWARE"
        })
        # Send the PDU to the IoT device
        client.sendWithPDUInfo("TRIGGER_RANSOMWARE", pduInfo)
        # Print a message to the console confirming that the ransomware trigger was sent
        print("Sent ransomware trigger command.")
        # Pause the loop for 10 seconds before sending the next PDU
        sleep(10)

# Check if the script is run as the main module and, if so, call the main function
if __name__ == "__main__":
    main()
