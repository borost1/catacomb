from asyncore import loop
from time import sleep
# import random, cmd, textwrap, sys, os, random, time
import catacomb_functions
from Catacomb_files import screens
from screens import door_questions
from screens import door_open_strings
from screens import door_closed_strings
import random
import asyncio

door_choices = {'a': 'first', 'b': 'second', 'c': 'third', 'd': 'fourth'}
action_choices = ['attack', 'befriend']

if __name__ == '__main__':

    print("\"\"\n"
          "\n"
          "\n"
          "  (`\ .-') /`   ('-.                                  _   .-')       ('-.         .-') _                       _   .-')      ('-.                 .-') _                      ('-.     .-') _      ('-.                            _   .-')   .-. .-')\n"
          "   `.( OO ),' _(  OO)                                ( '.( OO )_   _(  OO)       (  OO) )                     ( '.( OO )_   ( OO ).-.            (  OO) )                    ( OO ).-.(  OO) )    ( OO ).-.                       ( '.( OO )_ \  ( OO )\n"
          ",--./  .--.  (,------.,--.       .-----.  .-'),-----. ,--.   ,--.)(,------.      /     '._  .-'),-----.        ,--.   ,--.) / . --. / ,--. ,--.  /     '._          .-----.  / . --. //     '._   / . --. /   .-----.  .-'),-----. ,--.   ,--.);-----.\\n"
          "|      |  |   |  .---'|  |.-')  '  .--./ ( OO'  .-.  '|   `.'   |  |  .---'      |'--...__)( OO'  .-.  '       |   `.'   |  | \-.  \  |  | |  |  |'--...__)        '  .--./  | \-.  \ |'--...__)  | \-.  \   '  .--./ ( OO'  .-.  '|   `.'   | | .-.  |\n"
          "|  |   |  |,  |  |    |  | OO ) |  |('-. /   |  | |  ||         |  |  |          '--.  .--'/   |  | |  |       |         |.-'-'  |  | |  | | .-')'--.  .--'        |  |('-..-'-'  |  |'--.  .--'.-'-'  |  |  |  |('-. /   |  | |  ||         | | '-' /_)\n"
          "|  |.'.|  |_)(|  '--. |  |`-' |/_) |OO  )\_) |  |\|  ||  |'.'|  | (|  '--.          |  |   \_) |  |\|  |       |  |'.'|  | \| |_.'  | |  |_|( OO )  |  |          /_) |OO  )\| |_.'  |   |  |    \| |_.'  | /_) |OO  )\_) |  |\|  ||  |'.'|  | | .-. `.\n"
          "|         |   |  .--'(|  '---.'||  |`-'|   \ |  | |  ||  |   |  |  |  .--'          |  |     \ |  | |  |       |  |   |  |  |  .-.  | |  | | `-' /  |  |          ||  |`-'|  |  .-.  |   |  |     |  .-.  | ||  |`-'|   \ |  | |  ||  |   |  | | |  \  |\n"
          "|   ,'.   |   |  `---.|      |(_'  '--'\    `'  '-'  '|  |   |  |  |  `---.         |  |      `'  '-'  '       |  |   |  |  |  | |  |('  '-'(_.-'   |  |         (_'  '--'\  |  | |  |   |  |     |  | |  |(_'  '--'\    `'  '-'  '|  |   |  | | '--'  /\n"
          "'--'   '--'   `------'`------'   `-----'      `-----' `--'   `--'  `------'         `--'        `-----'        `--'   `--'  `--' `--'  `-----'      `--'            `-----'  `--' `--'   `--'     `--' `--'   `-----'      `-----' `--'   `--' `------'\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "              "
          )
    print()
    sleep(1.0)
    print()
    name = input('How can I call you?')
    print("You wake up in a dark room with 4 doors, labeled as; a, b, c, d.")
    sleep(2.0)
    print("This is not a good place to be, try to get out.")
    print()
    sleep(2.0)
    print()
    print("Good luck, " + name + " and don't fuck it up!")
    print()
    sleep(2.0)
    print()
    choice = input('Which door will you take? These doors are nasty, sometimes you need to try a door more than once.')
    print()
    sleep(2.0)
    print()

    catacomb_functions.which_door_opens()

    print()
    sleep(1.0)
    print()
    choice_action = input('You can attack or befriend them, which will it be?')
    print()
    sleep(1.0)
    print()

    flag = False
    while not flag:
        if choice_action.lower() not in action_choices:
            print('Invalid choice. Please choose "attack" or "befriend".')
            choice_action = input('Which will it be? ')
        else:
            if choice_action.lower() == action_choices[0]:
                print(catacomb_functions.attack_world1())

            elif choice_action.lower() == action_choices[1]:
                print(catacomb_functions.befriend_world1())
            flag = True
    print()
    sleep(2.0)
    print()
    next_choice = input(random.choice(screens.door_questions))
    while not flag:
        if random.random() < 0.75:
            door_closed_str = random.choice(door_closed_strings)
            print(door_closed_str)
            next_choice = input('Which door will you take?')
            while choice.lower() not in door_choices:
                print('Invalid choice. Please choose A, B, C, or D.')
                next_choice = input('Which door will you take?')
            chosen_door = door_choices[choice.lower()]
            print(f'You chose {chosen_door}.')  # embed the value of the chosen_door inside the string
        else:
            door_open_str = random.choice(door_open_strings)
            print(door_open_str)
            flag = True  # set the flag to True to exit the while loop
    while loop == 1:
        print(catacomb_functions.create_random_world1_screen())
        break

