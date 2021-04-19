import paho.mqtt.client as mqtt
from Resident import Resident

MQTT_BROKER = "localhost"
BASE_TEMPERATURE = 15

class Thermostat:
    def __init__(self):
        self.residentList = []
        self.Temperature = BASE_TEMPERATURE

    def addResident(self, name, temperature):
        self.residentList.append(Resident(name,temperature))

    def changeTemperature(self):
        residentsTemperature = []
        temp = 0
        for resident in self.residentList:
            if(resident.getLocation()):
                temp = resident.getTemperature()
                residentsTemperature.append(resident.getTemperature())
        if(len(residentsTemperature) == 0):
            self.Temperature = BASE_TEMPERATURE
        elif(len(residentsTemperature) == 1):
            self.Temperature = temp
        else:
            self.Temperature = sum(residentsTemperature)/len(residentsTemperature)
        self.showTemperature()

    def showTemperature(self):
        print("The Thermostat is set to: "+str(self.Temperature))

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("successful connection")
            client.subscribe("Resident")
            client.subscribe("Door")
            self.showTemperature()
        else:
            print("connection fail")

    def on_message(self, client, userdata, msg):
        print("log: "+msg.topic + " " + str(msg.payload))
        if(msg.topic == "Resident"):
            message = msg.payload.decode("utf-8").split()
            self.addResident(message[0],int(message[1]))
        elif(msg.topic == "Door"):
            message = msg.payload.decode("utf-8").split()
            for resident in self.residentList:
                if resident.name == message[0]:
                    if(message[1] == "in"):
                        resident.setLocation(True)
                    elif(message[1] == "out"):
                        resident.setLocation(False)
            self.changeTemperature()

if __name__ == '__main__':
    t = Thermostat()
    client = mqtt.Client()
    client.on_connect = t.on_connect
    client.on_message = t.on_message
    client.connect(MQTT_BROKER)
    client.loop_forever()


