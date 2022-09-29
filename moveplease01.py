#!/usr/bin/env python3
"""JMolato
   Moving and renaming files and folders"""

import shutil
import os

def main():
    # Change directory
    os.chdir('/home/student/mycode/')

    # Moving file/folder from a to b
    shutil.move('raynor.obj', 'ceph_storage/')

    # Prompt the user for file name
    xname = input('What is the new name for kerrigan.obj? ')
    
    # Ranaming file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
   
if __name__ == "__main__":
    main()

