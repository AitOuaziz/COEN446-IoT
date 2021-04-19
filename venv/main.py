#!/home/wa3ziz/coen446/mqtt/bin/python3
import paho.mqtt.client as mqtt
import subprocess

if __name__ == '__main__':
    subprocess.call(['gnome-terminal', '-t', 'Thermostat', '--','python3', 'Thermostat.py'])
    subprocess.call(['gnome-terminal', '-t', 'Management', '--','python3', 'Management.py'])



