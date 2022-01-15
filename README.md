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
### Raspberry is used for connection between Flight Controller and also laptop and the camera is also connected to the raspberry. All modules are stored and executed on Raspberry Pi. We used MAV-Link protocol for communication between a Ground Control Station, in our case this is raspberry and quadcopter Flight Controller. It is used to transmit the orientation of the vehicle, its GPS location and speed to the Flight Controller. GPS is connected to Flight Controller and located on the top position of drone to better receive current location. Then ESC converts the PWM signal from the flight controller or radio receiver, and drives the brushless motor by providing the appropriate level of electrical power. As firmware we used ArduPilot. Belowe is the scheme:

![image](https://user-images.githubusercontent.com/73778979/149628669-50bbbc8e-f110-40e8-b71d-c8a41af89bdb.png)

# Software (only code)

### Via paramiko (python library) we get the foundation for the high-level SSH library, which is used for common client as transferring files helper. (send txt file with coords to raspberry). For Drone functionality we used high-leve library DroneKit. 
### For this project we created two algorithms, which are deeply connected: algorithm of flight mission and algorithm of photo mapping.
## Mapping
### There is directory photos on the raspberry, where all photos appear. The thing is, all photos have special names, for example 11.jpg, 12.jpg, 23.jpg. Their names show their position on finaly merged big photo. 11.jpg means, that its position is top left corner, 12.jpg is to the right of 11.jpg, 21.jpg is below and so on. That's how we get big merged photo.
## Flight mission
### Now about mission algorithm. It consists of 3 parts.
### 1) We get coordinates of 4 dots on the map from the .txt file. Then function center_finder() calculates coordinates of points, where our drone has to make a photo. The drone takes off and climbs on certain high. After that, he flies to the first point, mentioned in .txt, and then flies to 3rd point in .txt. He does it to find correct angle relative to North to be able to make all photos in correct orientation.
![image](https://user-images.githubusercontent.com/76886116/149629455-f2c265d9-a16c-4ca4-acda-3f86f32556c2.jpeg)
### 2) After that drone gets to the first center (first point, where it has to take a photo)
![image](https://user-images.githubusercontent.com/76886116/149629509-61124948-26df-4f75-be17-608ecbe6ba80.jpeg)
### 3) When drone is on first center, he does for each center: rotates to correct orientation, takes a photo and flies to next center.
![image](https://user-images.githubusercontent.com/76886116/149629577-844c367a-69b1-4c6d-ad9d-c7b3e12dfb35.jpeg)
### Finally, when the last photo is taken, drone merges all photos into one and returns to the base coordinates.

# Implemented and Results

### The drone is built and working, however, the reason why the drone can't perform the flight safely is that the voltage on one ESC is 0.7 V and on other 1.5.

# Contributors
- https://github.com/Vl-tb
- https://github.com/stepansushko1
- https://github.com/vilgurin
- https://github.com/msharsh
