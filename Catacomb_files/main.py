from asyncore import loop
from time import sleep
# import random, cmd, textwrap, sys, os, random, time
import catacomb_functions
import inventory
from tqdm import tqdm
import asyncio
from tqdm.asyncio import tqdm, trange
import itertools
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
    sleep(3.0)
    print()
    name = input('How can I call you?')
    print("You wake up in a dark room with 4 doors, labeled as; a, b, c, d.")
    sleep(3.0)
    print("This is not a good place to be, try to get out.")
    print()
    sleep(3.0)
    print()
    print("Good luck, " + name + " and don't fuck it up!")
    print()
    sleep(3.0)
    print()
    choice = input('Which door will you take? These doors are nasty, sometimes you need to try a door more than once.')
    print()
    sleep(3.0)
    print()

    count = 0
    while inventory.player.hp > 0:
        total = 0
        for num in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            sleep(0.25)
            total = total + num

        catacomb_functions.which_door_opens()
        screen_str, random_obstacle = catacomb_functions.create_random_world1_screen()

        print()
        sleep(3.0)
        print()
        print('You can attack or befriend them.')
        print()
        sleep(3.0)
        print()

        catacomb_functions.get_action_choice()

        print()
        sleep(3.0)
        print()
        print()
        sleep(3.0)
        print()

        count += 1
        if count % 3 == 0:
            print(random.choice(screens.catacomb_facts))

        elif count % 5 == 0:
            # every 5 times the loop runs
            catacomb_functions.level_up_obstacles(screens.defeated_obstacles)

        if inventory.player.hp <= 0:
            break

    # execute another function after the loop is done
    catacomb_functions.game_over()
