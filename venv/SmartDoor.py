import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.2.82"

class SmartDoor:
    def __init__(self):
        self.greeting()

    def greeting(self):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("- Welcome to the Management App                             -")
        print("+ Use: move Name Location - to move a resident              +")
        print("+ Name: name of a resident                                  +")
        print("- Location: ""in"" or ""out""                               -")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print()


if __name__ == '__main__':
    client = mqtt.Client()
    d = SmartDoor()
    client.connect(MQTT_BROKER)