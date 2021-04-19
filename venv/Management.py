from Resident import Resident
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
AUTH = {
    "username": "admin",
    "password": "admin"
}

class Management:
    def __init__(self):
        self.greeting()
        self.residentList = []

    def addResident(self, name, temperature):
        self.residentList.append(Resident(name,temperature))
        payload = name+" "+str(temperature)
        publish.single(topic="Resident", payload=payload, hostname=MQTT_BROKER)
        print("Topic: Resident, Payload: "+payload+ ". To: "+MQTT_BROKER)
        print(name + " has been added!")

    def removeResident(self, name):
        for resident in self.residentList:
            if resident.name == name:
                self.residentList.remove(resident)

    def printResident(self):
        for resident in self.residentList:
            print(resident)
        print()

    def greeting(self):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("- Welcome to the Management App                             -")
        print("+ Use: add Name Temperature - to add a resident             +")
        print("- Use: quit - Quit the Management app                       -")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()

if __name__ == '__main__':
    client = mqtt.Client()
    m = Management()
    client.connect(MQTT_BROKER)
    command = input("Please type a command: ")
    while (command.lower() != "quit"):
        if(command.lower().startswith("add")):
            name = command.split()[1]
            temperature = command.split()[2]
            m.addResident(name, int(temperature))
        command = input("Please type a command: ")


