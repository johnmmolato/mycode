#!/usr/bin/env python3
"""JMolato
   Exploring network interfaces"""

import netifaces

def main():
    print(netifaces.interfaces())
    
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            # This print statement will always print MAC without an end of line
            print('MAC: ', end='')
            # Prints the MAC address
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            # This print statement will always print IP without an end of line
            print('IP: ', end='')
            # Prints the IP address
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            # Print an error message
            print('Could not collect adapter information')



if __name__ == "__main__":
    main()
