# Quad-Drone
### Principles of Computer Organization Project

# General Description
### During the semester we were constructing and programming a drone (quadcopter) capable of automatically flying over a given area, take photos and generate a 2D map from them and send back above-mentioned map to the server (laptop).

# Components
### Drone Frame
### Flight Controller H743-SLIM
### GPS: Flywoo gm8-5883
### Raspberry pi 3
### Pi camera 3
### ESC Skywalker 

# How it is working?

### There are two main parts of project: Software and Hardware.

# Hardware 
### Raspberry is used for connection between microcontroler and also laptop and the camera is also connected to the raspberry. All modules are stored and executed on Raspberry Pi. We used MAV-Link protocol for communication between a Ground Control Station, in our case this is raspberry and quadcopter microcontroller. It is used to transmit the orientation of the vehicle, its GPS location and speed to the Flight Controller. GPS is connected to microcontroler and located on the top position of drone to better receive current location. As firmware we used ArduPilot. Belowe is the scheme:

# Software (only code)

### Via paramiko (python library) we get the foundation for the high-level SSH library, which is used for common client as transferring files helper. (send txt file with coords to raspberry). For Drone functionality we used high-leve library DroneKit. 


# Implemented and Results

### The drone is built and working, however, the reason why the drone can't perform the flight safely is that the voltage on one ESC is 0.7 V and on other 1.5.

# Contributors
- https://github.com/Vl-tb
- https://github.com/stepansushko1
- https://github.com/vilgurin
- https://github.com/msharsh
