import random as r
from collections import defaultdict


from ziagent_game.common import *


class Agent(object):
    """
    Object class for agents.
    Agents are made of:
        id
        total payoff -- winnings from all games
        games played -- list of game id, move, payoff
    """
    instances = {}

    def __init__(self):
        self.total_payoff = 0
        self.games_played = []

        self.get_id()
        self.__class__.instances[self.id] = self

    def generate_move(self):
        self.move = r.choice(move_choices)
        return self.move

    def get_id(self):
         self.id = get_id(self.__class__)

    # TODO: Create evaluation of previous_moves