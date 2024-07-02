# Import the required modules for handling time delays, TCP communication, and simulation-specific tasks
from time import sleep
from tcp import *
from simulation import *

# Define the port on which the IoT device will listen for incoming connections
port = 1025
# Define the protocol and PDU type used for communication with Malicious Host
protocolName = "MyProtocol2"
pduType = "Ransomware"
# Define the color used for the PDU for visualization
pduColor = 0xff00ff

# Instantiate a TCPServer object to manage IoT device operations
server = TCPServer()

# Define the function that will be called when Malicious Hostt connects to the server
def onTCPNewClient(client):
    # Define a nested function for handling changes in the TCP connection state
    def onTCPConnectionChange(type):
        # When the connection state changes, print a message with the Malicious Host's remote IP and the new state
        print("Connection to " + client.remoteIP() + " changed to state " + str(type))

    # Define a nested function to handle data received from the Malicious Host, along with PDU information
    def onTCPReceiveWithPDUInfo(data, pduInfo):
        # Print a message displaying the Malicious Host's IP and the data received
        print("Received from {} with data: {}".format(client.remoteIP(), data))
        # Check if the received data is a "trigger_ransomware" command
        if data.strip().lower() == "trigger_ransomware":
            # If the command is received, print a simulated ransomware message
            print("""
            WARNING: Your server has been compromised.
            All your data has been encrypted.

            To restore your system, you must pay 0.1 Bitcoin to the following address:
            1BoatSLRHtKNngkdXEeobR76b53LETtpyT

            Instructions on how to acquire and transfer Bitcoin have been sent to your administrator's email address.
            Attempting to remove the software or shutting down the system will result in permanent data loss.
            Your compliance is necessary to ensure the recovery of your data.
            """)
        # Add messages to the PDU information acknowledging reception and processing of the command
        pduInfo.addInMessage("Received your command.")
        pduInfo.addOutMessage("Processed your command.")
        # Set the PDU format for the reply to indicate that the command was processed
        pduInfo.setOutFormat(protocolName, pduType, {"type": "REPLY", "data": "Command processed"})
        # Send a response back to the Malicious Host with the updated PDU information
        client.sendWithPDUInfo("Command processed", pduInfo)

    # Register the above nested functions as callbacks to handle events for each client
    client.onConnectionChange(onTCPConnectionChange)
    client.onReceiveWithPDUInfo(onTCPReceiveWithPDUInfo)

# Define a setup function to initialize the server and configure PDUs
def setup():
    # Add a custom PDU format to the simulation with specific fields and properties
    Simulation.addCustomPDU(protocolName, pduType, {
        "title": "My PDU2",
        "units": "Bits",
        "unit_marks": [16],
        "width": 32,
        "fields": [
            {"value": "TYPE: {type}", "size": 32},
            {"value": "DATA: {data}", "size": 32}
        ]
    })
    # Print a message indicating that the server is starting and on which port it's listening
    print("Starting server on port", port)
    # Register the function to handle Malicious Host connections
    server.onNewClient(onTCPNewClient)
    # Start listening for incoming connections on the specified port
    server.listen(port)

# Call the setup function to start the IoT Device server
if __name__ == "__main__":
    setup()
    # Enter an infinite loop to keep the IoT Device server running, checking for new connections or data every 10 seconds
    while True:
        sleep(10)
