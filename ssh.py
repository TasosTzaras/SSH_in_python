#!/usr/bin/env python3

import os

user = input("Give Username: ")
server = input("Give Server: ")

os.system('ssh '+ "%s@%s" %(user, server))
