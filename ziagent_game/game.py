
import random as r
from collections import deque

from ziagent_game.agents import Agent
from ziagent_game.common import *

class Game(object):
    "Object class for games."
    instances = {}

    def __init__(self, players):
        self.a1 = players[0].id
        self.a2 = players[1].id
        self.a1_move = players[0].move
        self.a2_move = players[1].move
        self.a1_result, self.a2_result = self.play(self.a1_move, self.a2_move)

        self.get_id()
        self.__class__.instances[self.id] = self

    def get_id(self):
        self.id = get_id(self.__class__)

    def play(self, a1_move, a2_move):
        # TODO: Add game logic. 
        a1_result = a2_result = 0
        return a1_result, a2_result