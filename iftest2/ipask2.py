#!/usr/bin/env python3
"""JMolato
   Conditinals - testing if strings test true"""

def main():
    ipchk = input("Apply an IP address: ") # this line now prompts the user for input

    # if user set IP of gateway
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    # if any data is provided, this will test true
    elif ipchk:
        print("Looks like the IP address was set: " + ipchk) # indented under if
    # if data is NOT provided 
    else:
         print("You did not provide input.") # indented under else

if __name__ == "__main__":
    main()
