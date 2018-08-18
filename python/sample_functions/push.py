#!/usr/bin/env python

# Function to create the list of commands
def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
    return commands

# Function to print the command being 'sent'
def push_commands(device, commands):
    print('Connecting to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)

if __name__ == "__main__":

    devices = ['switch1', 'switch2', 'switch3']

    vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'}, {'id': '30', 'name': 'WLAN'}]

    for vlan in vlans:
        vid = vlan.get('id')
        name = vlan.get('name')
        print('\n')
        commands = get_commands(vid, name)
        for device in devices:
            push_commands(device, commands)
            print('\n')