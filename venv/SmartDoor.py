import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"

class SmartDoor:
    def __init__(self):
        self.greeting()

    def greeting(self):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("- Welcome to Smart Door                                     -")
        print("+ Use: quit - Quit the Management app                       +")
        print("- Use: move Name Location - to move a resident              -")
        print("+ Name: name of a resident                                  +")
        print("- Location: ""in"" or ""out""                               -")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()


if __name__ == '__main__':
    client = mqtt.Client()
    d = SmartDoor()
    client.connect(MQTT_BROKER)
    command = input("Please type a command: ")
    while (command.lower() != "quit"):
        if (command.lower().startswith("move")):
            name = command.split()[1]
            location = command.split()[2]
            payload = name + " " + location
            publish.single(topic="Door", payload=payload, hostname=MQTT_BROKER)
        command = input("Please type a command: ")