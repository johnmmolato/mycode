#!/usr/bin/env python3
"""JMolato
   Parsing log files and logging success logins"""

def main():

    # parse keystone.common.wsgi and return the number of success login attempts
    successlog = 0 # initial count for success log

    # open the file for reading

    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

            # loop over the file
            for suc in kfile:
                # if this "loaded" appears in the line
                if "- - - - -] Loaded" in suc:
                    successlog += 1

    print("The number of successful login attempts is", successlog)

if __name__ == "__main__":
    main()
