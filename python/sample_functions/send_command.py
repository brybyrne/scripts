#!/usr/bin/env python


"""This is a very (very) basic example of feeding arguments to populate fields in a script.
The format used will be 'send_commands.py username password ip_address subnet_mask'
"""

import sys

if __name__ == "__main__":
    args = sys.argv
    print("Username: " + args[1])
    print("Password: " + args[2])
    print("IP Address: " + args[3])
    print("Subnet Mask: " + args[4])