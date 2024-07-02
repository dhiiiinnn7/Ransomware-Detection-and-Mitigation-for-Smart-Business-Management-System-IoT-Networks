# Ransomware Detection and Mitigation for Smart Business Management System IoT Networks

## Overview

This project focuses on the critical issue of ransomware detection and mitigation within Smart Business Management Systems (SBMS) enhanced by Internet of Things (IoT) networks. By leveraging Cisco Packet Tracer, this project simulates various security scenarios to protect IoT networks from ransomware attacks. The simulations include implementations of firewalls, Intrusion Detection and Prevention Systems (IDPS), and Software-Defined Networking (SDN), both individually and in combination, to demonstrate a multi-layered security approach.

## Table of Contents

- [Brief Explanation](#brief-explanation)
- [Project Structure](#project-structure)
- [Scenarios](#scenarios)
  - [Scenario 1: Basic Setup with Ransomware Payload](#scenario-1-basic-setup-with-ransomware-payload)
  - [Scenario 2: Implementation of Firewall](#scenario-2-implementation-of-firewall)
  - [Scenario 3: Implementation of IDPS](#scenario-3-implementation-of-idps)
  - [Scenario 4: Implementation of SDN](#scenario-4-implementation-of-sdn)
  - [Scenario 5: Combined Security Features](#scenario-5-combined-security-features)
- [IoT Device Scripts](#iot-device-scripts)
- [Installation and Setup](#installation-and-setup)
- [Running the Simulations](#running-the-simulations)
- [Evaluation](#evaluation)
- [References](#references)
- [License](#license)

## Brief Explanation

The project sets up a series of network configurations in Cisco Packet Tracer to simulate how different security measures can detect and mitigate ransomware attacks. Each scenario builds upon the previous one, starting from a basic network setup with no security measures to a final scenario that integrates firewalls, IDPS, and SDN for comprehensive protection.

The purpose of this project is to explore and evaluate the effectiveness of different security mechanisms in protecting IoT networks from ransomware attacks. By simulating real-world attack scenarios and implementing various security measures, the project aims to provide insights into how to design and secure IoT networks against sophisticated cyber threats.

This project helps network administrators and security professionals understand the practical applications and benefits of implementing multiple security layers within IoT networks. It demonstrates:
- The vulnerabilities of IoT networks to ransomware attacks.
- The effectiveness of individual security measures such as firewalls, IDPS, and SDN.
- The enhanced security achieved through a combined, multi-layered approach.
- Practical configurations and scripts for deploying security measures in a simulated environment.

By providing detailed configurations and scripts, the project serves as a valuable resource for those looking to improve their network security posture against ransomware and other cyber threats.

## Project Structure

### Routers and Firewall Configurations

- `ROUTER1_startup-config.txt`: Startup configuration for Router 1.
- `ROUTER2_startup-config.txt`: Startup configuration for Router 2.
- `ROUTER3_startup-config.txt`: Startup configuration for Router 3.
- `IDPS ROUTER_startup-config.txt`: Startup configuration for the IDPS Router.
- `FIREWALL1_startup-config.txt`: Startup configuration for Firewall 1.
- `FIREWALL2_startup-config.txt`: Startup configuration for Firewall 2.

### IoT Devices Programming
- `Fire.js`: JavaScript code for fire detection.
- `ID CARD - STAFF.py`: Python code for staff ID card simulation.
- `ID CARD - UNAUTHORISED.py`: Python code for unauthorized ID card simulation.
- `ID CARD READER.py`: Python code for ID card reader simulation.
- `MCU 3 - Temperature Monitor.py`: Python code for temperature monitoring.
- `RESTRICTED AREA DOOR.py`: Python code for restricted area door control.
- `SBC 1 - Fire Alert.py`: Python code for fire alert system.
- `SBC 1 - Motion Alert.py`: Python code for motion alert system.
- `RANSOMWARE PAYLOAD BY MALICIOUS HOST.py`: Python code for the main ransomware payload.
- `RANSOMWARE PAYLOAD - Server.py`: Python code simulating ransomware behaviour.

### Packet Tracer Scenarios

- `Scenario 1 - Ransomware Payload.pkt`: Cisco Packet Tracer file for Scenario 1.
- `Scenario 2 - Firewall.pkt`: Cisco Packet Tracer file for Scenario 2.
- `Scenario 3 - IDPS.pkt`: Cisco Packet Tracer file for Scenario 3.
- `Scenario 4 - SDN.pkt`: Cisco Packet Tracer file for Scenario 4.
- `Scenario 5 - Final - Ransomware Detection and Mitigation for Smart Business Management System IoT Network.pkt`: Cisco Packet Tracer file for Scenario 5.

- `Dhin Islam Md - 001115470- Ransomware Detection and Mitigation for Smart Business Management System IoT Networks Control and Security.pdf`: Detailed project report.

## Scenarios

### Scenario 1: Basic Setup with Ransomware Payload

In this scenario, a basic network setup is created without any security implementations. The ransomware payload is configured to demonstrate the vulnerability of the system.

### Scenario 2: Implementation of Firewall

This scenario involves the implementation of firewall rules to protect the network. The firewall configuration aims to prevent unauthorized access and block malicious traffic.

### Scenario 3: Implementation of IDPS

An Intrusion Detection and Prevention System (IDPS) is implemented in this scenario. The IDPS monitors network traffic for suspicious activities and takes actions to prevent potential ransomware attacks.

### Scenario 4: Implementation of SDN

Software-Defined Networking (SDN) is used to enhance network management and security. This scenario demonstrates the use of SDN to dynamically control network traffic and mitigate ransomware threats.

### Scenario 5: Combined Security Features

The final scenario integrates all three security features (Firewall, IDPS, and SDN) to provide a robust and multi-layered defense against ransomware attacks. This scenario demonstrates the effectiveness of a comprehensive security strategy.

## IoT Device Scripts

- **Fire.js**: This script is responsible for controlling the fire detection sensors within the IoT network. It monitors the environment for signs of fire and triggers alerts when specific conditions are met.

- **ID CARD - STAFF.py**: This Python script simulates the behavior of an authorized staff ID card. It interacts with the ID card reader to allow access to restricted areas for verified personnel.

- **ID CARD - UNAUTHORISED.py**: This script simulates the behavior of an unauthorized ID card. It is used to test the system's ability to deny access to unauthorized individuals attempting to enter restricted areas.

- **ID CARD READER.py**: This script manages the functionality of the ID card reader device. It reads the ID card information, verifies its authenticity, and grants or denies access based on the credentials.

- **MCU 3 - Temperature Monitor.py**: This script is used to monitor and control the room temperature. It collects temperature data from sensors and can trigger alerts or actions if the temperature goes beyond predefined thresholds.

- **RESTRICTED AREA DOOR.py**: This script controls the access to restricted areas by managing the door mechanism. It ensures that only authorized personnel with valid ID cards can enter these areas.

- **SBC 1 - Fire Alert.py**: This script manages the fire alert system. It processes data from fire detection sensors and triggers alarms and notifications to alert users and administrators of potential fire hazards.

- **SBC 1 - Motion Alert.py**: This script controls the motion detection alert system. It monitors the environment for any unauthorized movement and triggers alerts to notify security personnel of potential intrusions.

- **RANSOMWARE PAYLOAD BY MALICIOUS HOST.py**: This is the main ransomware payload script used by the malicious host. It establishes a connection with the target IoT device and sends commands to trigger ransomware attacks, demonstrating the network's vulnerability and testing the implemented security defenses.

- **RANSOMWARE PAYLOAD - Server.py**: This script simulates ransomware behaviour. It mimics the actions of ransomware on the network, such as encrypting files and demanding ransom, to test the effectiveness of the implemented security measures.

## Installation and Setup

### Clone the Repository

   ```bash
   git clone https://github.com/dhiiiinnn7/Ransomware-Detection-and-Mitigation-for-Smart-Business-Management-System-IoT-Networks.git
   cd Ransomware-Detection-and-Mitigation-for-Smart-Business-Management-System-IoT-Networks
  ```

### Set Up Cisco Packet Tracer

Ensure Cisco Packet Tracer is installed on your system to run the provided .pkt simulation files.

### Set Up IoT Device Scripts

Deploy the provided Python and JavaScript scripts to the respective IoT devices within the Packet Tracer simulations.

## Running the Simulations

- Open the appropriate .pkt file in Cisco Packet Tracer.
- Ensure all devices are configured correctly with the provided startup configuration files.
- Run the simulation to observe the network behaviour under different security implementations.

## Evaluation

The project evaluates the effectiveness of different security measures in mitigating ransomware attacks. Each scenario is tested for its ability to detect and prevent ransomware activities, with performance metrics such as response time, accuracy, and overall network security being analyzed.

## References
Refer to the detailed project report provided in Dhin Islam Md - Ransomware Detection and Mitigation for Smart Business Management System IoT Networks Control and Security.pdf for an in-depth analysis, including:

- Background and significance of the study.
- Methodologies used for implementing and testing the scenarios.
- Detailed findings and discussions on the effectiveness of each security measure.

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
