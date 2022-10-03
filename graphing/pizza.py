#!/usr/bin/env python3
"""JMolato
   Pizza exercise"""

import matplotlib.pyplot as plt
import time as t
def main():
    print("Welcome to Big pa John pizza!",flush=True)
    t.sleep(2)
    answer = input("Would you like some pizza?").lower()
    if answer == "yes":    
        topping1, topping2, topping3, topping4 = input("Please provide 4 different toppings you want on your pizza?").split()
        slices = list(map(int, input("Provide the size of the slices, i.e 20,30,64 ").split()))   
        print("Your pizza is baking and will be done in 5 seconds", flush=True)
        t.sleep(1)
        print("4", flush=True)
        t.sleep(1)
        print("3", flush=True)
        t.sleep(1)
        print("2", flush=True)
        t.sleep(1)
        print("1", flush=True)
        t.sleep(1)
        print("Your pizza is done, enjoy!")
    if answer == "no":
        ("No pizza for you!")

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = topping1, topping2, topping3, topping4
    sizes = slices
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig("/home/student/static/perfectPizza.png")

if __name__ == "__main__":
    main()
