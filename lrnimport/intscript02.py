#!/usr/bin/env python3
"""JMolato
   Scripting command with python"""

import subprocess  ## <-------- changed
def main():

    subprocess.call(["ip", "link", "show", "up"])
    print("This program will check your interfaces.")
    interface = input("Enter an interface, like, ens3: ")
    subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
    subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed

if __name__ == "__main__":
    main()
