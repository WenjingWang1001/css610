import random as r
from collections import defaultdict
import weakref


from ziagent_game.common import *


class Agent(object):
    "Object class for agents."
    instances = {}

    def __init__(self):
        
        self.move = r.randint(0,1)
        self.previous_moves = []

        self.get_id()
        self.__class__.instances[self.id] = self

    def generate_move(self):
        previous_move = self.move
        self.previous_moves.append(previous_move)
        
        self.move = r.choice(move_choices)

    def get_id(self):
         self.id = get_id(self.__class__)