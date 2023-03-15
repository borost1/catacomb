from time import sleep
# import random, cmd, textwrap, sys, os, random, time
import catacomb_functions
from screens import world
from screens import door_open_strings
from screens import door_closed_strings
import random

door_choices = {'a': 'first', 'b': 'second', 'c': 'third', 'd': 'fourth'}

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

    # Randomly select a string to print
    loop = 1

    flag = False  # control mechanism, to exit the loop as conditions are met, common name for that

    while not flag:
        if random.random() < 0.75:
            door_closed_str = random.choice(door_closed_strings)
            print(door_closed_str)
            choice = input('Which door will you take?')
            while choice.lower() not in door_choices:
                print('Invalid choice. Please choose A, B, C, or D.')
                choice = input('Which door will you take?')
            chosen_door = door_choices[choice.lower()]
            print(f'You chose {chosen_door}.')  # embed the value of the chosen_door inside the string
        else:
            door_open_str = random.choice(door_open_strings)
            print(door_open_str)
            flag = True  # set the flag to True to exit the while loop

    while loop == 1:
        print(catacomb_functions.create_random_world1_screen())
        break





