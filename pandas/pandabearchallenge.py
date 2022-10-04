#!/usr/bin/env python3
"""JMolato
   Panda challenge 1 - transform between json,csv and excell"""

import pandas as pd

def main():

    # create a dataframe from json
    df = pd.read_json("5movies.json")
    # create a dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()


