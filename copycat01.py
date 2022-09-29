#!/usr/bin/env python3
"""JMolato
   Copying files and folders"""

# import additional code to complete our task
import shutil
import os

def main():
    # Move into a working Directory
    os.chdir("/home/student/mycode/")

    # Copy file a to b
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # Copy the entire directorya to directoryb
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

# main guard
if __name__ == "__main__":
    main()

