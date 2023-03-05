from time import sleep
#import random, cmd, textwrap, sys, os, random, time
import screens
import catacomb_functions
import inventory
door_choice_A = ['a', 'first', 'A', 'First']
door_choice_B = ['b', 'second', 'B', 'Second']
door_choice_C = ['c', 'third', 'C', 'Third']
door_choice_D = ['d', 'fourth', 'D', 'Fourth']



if __name__ == '__main__':

        print("Welcome to the Maut Catacomb!")
        print()
        sleep (1.0)
        print()
        name = input('How can I call you?')
        print("You wake up in a dark room with 4 doors, labeled as; a, b, c, d.")
        sleep (2.0)
        print("This is not a good place to be, try to get out.")
        print()
        sleep (2.0)
        print()
        print("Good luck, " + name + " and don't fuck it up!")
        print()
        sleep(2.0)
        print()
        choice = input('Which door will you take?')
        if choice in door_choice_A:
                print('The door opens')
        elif choice in door_choice_B:
                print('This door would not budge')
        elif choice in door_choice_C:
                print('This one needs a key probably')
        elif choice in door_choice_D:
                print('Wait,this is the wall painted as a door')



        if world == 1 and choice in door_choice_A:
                #call level function



#ami a main-en kivul hozok letre, az globalisan elerheto, main-en belul nem elerheto mashol