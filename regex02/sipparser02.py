#!/usr/bin/python3
"""Jmolato
   Learning regex to seach text"""

# Python standard library
import re

def main():
    # open the networktrace (text format)
    with open('networktrace.txt') as trace:
        # loop across the text file
        for line in trace:
            # look for a line that begins with sip:+ followed by digits@IP:port
            conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', line)
            if conobj:
                print(conobj.group())
                print("The phone number is: ", end="")
                print(conobj.group(1))
                print("The IPv6 is: ", end="")
                print(conobj.group(2))
                print("The port is: ", end="")
                print(conobj.group(3))
if __name__ == "__main__":
    main()

