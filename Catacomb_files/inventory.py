from typing import List, Any


class player:
    lives = 3
    game_level: ''

    def __init__(self):
        self.name = '',
        self.hp = 100,
        self.points = 0,
        self.lives = 3,
        self.inventory = []
        self.location = ''
        self.solved_places = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False,
                          10: False, 11: False, 12: False}
        
        # this might not be right in here, but I def. need it somewhere,
    # id of screens and bulian, need to access it in higher levels as well, eleg lehet felsorolni hogy mik lettek
    # megoldva,
    # nem kell False/true
myPlayer = player()

class Obstacle:
  level = ''

  def __init__(self, name, type, level):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_active = True

  def __repr__(self):
      return 'This obstacle is called {name}, you are on level {level}, facing a {type} type creature!'.format \
        (level = self.level, name = self.name, health = self.health, type = self.type)


a_o = Obstacle("Skeleton", "Death", 7)
b_o = Obstacle("Sphynx", "Riddle", 0)
c_o = Obstacle("Ghost", "Dark", 9)
d_o = Obstacle("Sufi", "Spiritual", 10)
e_o = Obstacle("Frog", "Water", 3)
f_o = Obstacle("Portuguese man o' war", "Water", 8)

defeated_obstacles = []
