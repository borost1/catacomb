# import path from screens just like a module
import screens
from inventory import player
import inventory
from inventory import Obstacle

import random


# modify the function to return a string with the screen information
def create_random_world1_screen():
    """creates a random screen, importing from the screens file"""
    title = random.choice(screens.titles)
    description = random.choice(screens.description)
    obstacle = random.choice(screens.obstacles)
    doors = random.sample(screens.doors, 4)
    screen_id = random.randint(1000, 9999)
    screens.screens_id.append(screen_id)  # append screen_id to the list
    # create a string with the screen information
    screen_str = f"You are in {title}. This place is {description} You see a {obstacle}, what do you do?"
    # return the string
    return screen_str






# call the function to generate a random screen and print the result
print(create_random_world1_screen())


screen = {
        "id": screens.screens_id,
        "title": screens.titles,
        "description": screens.description,
        "obstacle": screens.obstacles,
        "doors": screens.doors
    }




def lose_health(self, amount):
    """Reduces the player's health by the given amount."""
    self.health -= amount
    if self.health <= 0:
        print(f"{self.name} has died!")
    else:
        print(f"{self.name} has {self.health} health remaining.")


def gain_health(self, amount):
    """Increases the player's health by the given amount."""
    self.health += amount
    print(f"{self.name} has gained {amount} health. {self.name} now has {self.health} health.")


def level_up_obstacles(defeated_obstacles):
    """Levels up the obstacles"""
    count_list_elements = lambda x: len(x)
    for obstacle in defeated_obstacles:
        if count_list_elements(defeated_obstacles) > player.game_level:
            Obstacle.level += 4
    return Obstacle.level


def game_over():
    """if player is dead, game end"""
    if player.lives == 0:
        print('''
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄ ''')
