#!/usr/bin/env python3
"""JMolato
   Working with list objects and methods"""

def main():
    proto = ["ssh", "http", "https"]
    print(proto)
    print(proto[1])
    proto.extend("dns") 
    print(proto)

main()
