# COEN 446 Internet of Things (Project)
## Table of contents
* [General info](#general-info)
  
* [Technologies](#technologies)

* [Setup](#setup)

* [Usage](#usage)
---

## General info
This project is an implementation of a house smart heating/cooling 
system. We are using the MQTT protocol to implement communication 
between the different sub-systems. The different components are:
* Management App (Management.py): This entity implement the addition
  of new resident to the house. An addition is composed of a name and a 
  preferred temperature. For every addition, this entity will publish
  to the broker under the topic *Resident*.
* Smart door locker (SmartDoor.py): This entity implement the movement
of resident through the house door. Once a resident is added via the
  Management app, he is considered to be outside. Every time the 
  position of a resident is changed, this entity will publish it to the 
  broker under the topic *Door*.
  
* Thermostat (Thermostat.py): This entity implement the temperature
set by the smart thermostat. It subscribes to the topic *Resident* to
  keep track of the people it should interact with. It subscribes to the
  topic *Door* to adjust the house temperature according to how is 
  inside.
  
## Technologies
Project is created with:
* [Python: 3.8](https://www.python.org/downloads/release/python-386/)
* [paho-mqtt: 1.5.1](https://pypi.org/project/paho-mqtt/)
* [Mosquitto: 2.0](https://mosquitto.org/download/)

This project is meant to run on an Ubuntu 20.04 machine, with the above 
software installed.

## Setup
All the steps below are done in the terminal.
* Update Ubuntu
```sh
sudo apt update
```
* Install Python 3.8 and pip3
```sh
sudo apt install python3 python3-pip
```
* Install Mosquitto (mqtt broker)
```sh
sudo apt install mosquitto
```
* Install paho-mqtt (mqtt client for Python)
```sh
pip3 install paho-mqtt
```

## Usage
To run this project, in a terminal run the follow:
```sh
python3 main.py
```
All the source file (*.py) of this project must be in the same directory.

### Note
To use an external mqtt broker, you must change the value of `<MQTT_BROKER>`
inside the files Management.py, SmartDoor.py and Thermostat.py to the
ip address of the broker of your choice.




