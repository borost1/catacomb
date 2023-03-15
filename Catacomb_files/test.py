from time import sleep
import catacomb_functions
from screens import world
from screens import door_open_strings
from screens import door_closed_strings
import random

door_choice_A = ['a', 'first', 'A', 'First']
door_choice_B = ['b', 'second', 'B', 'Second']
door_choice_C = ['c', 'third', 'C', 'Third']
door_choice_D = ['d', 'fourth', 'D', 'Fourth']

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
    choice = input('Which door will you take?')
    print()
    sleep(2.0)
    print()

    while world == 1 and choice in [door_choice_A, door_choice_B, door_choice_C, door_choice_D]:
        catacomb_functions.create_random_world1_screen()

        # Randomly select a string to print
        if random.random() < 0.75:
            door_closed_str = random.choice(door_closed_strings)
            print(door_closed_str)
        else:
            door_open_str = random.choice(door_open_strings)
            print(door_open_str)