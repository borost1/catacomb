
#import path from screens just like a module

import main
from inventory import player
import inventory
import screens
from inventory import Obstacle

import random

from screens import titles, obstacles, doors, description

def create_random_world1_screen():
    """"creates a random screen, importing from the screens file"""
    title = random.choice(titles)
    description = random.choice(description)
    obstacle = random.choice(obstacles)
    doors = random.sample(doors, 4)
    screen_id = random.randint(1000, 9999)

    screen = {
        "id": screen_id,
        "title": title,
        "description": description,
        "obstacle": obstacle,
        "doors": doors
    }

    return screen


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




















