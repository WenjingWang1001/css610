
import random as r
from collections import deque

from ziagent_game.agents import Agent
from ziagent_game.common import *

class Game(object):
    """
    Object class for games.
    Games are made of:
        2 players
        a move for each player
        a resulting payoff for each player
    """
    instances = {}

    def __init__(self, players, time):
        self.a1 = players[0]
        self.a2 = players[1]
        self.a1_move = None
        self.a2_move = None
        self.a1_pay = None
        self.a2_pay = None
        self.time = time

        self.get_id()
        self.play(players)
        
        self.__class__.instances[self.id] = self

    def __repr__(self):
        'Str representation of the game.'
        values = (str(self.a1.id), str(self.a1_move[0]),
                  str(self.a2.id), str(self.a2_move[0]), 
                  str(self.a1_pay), str(self.a2_pay))
        return 'a1: %s %s, a2: %s %s, a1 playoff: %s, a2 playoff %s' % values

    def get_id(self):
        'Generates id for the game.'
        self.id = get_id(self.__class__)

    def play(self, players):
        """
        Plays a game. 
        * First both player generate a move.
        * Then pay_offs are calculated.
          - Playoff results are saved so that the agent may reflect 
            at their success or lack there of. 
        """
        self.a1_move = self.a1.generate_move()
        self.a2_move = self.a2.generate_move()

        for pay in payoffs:

            if (self.a1_move[1], self.a2_move[1]) == pay[0]:
                a1_pay = self.a1_pay = pay[1][0]
                a2_pay = self.a2_pay = pay[1][1]

                self.a1.games_played.append((self.id, self.a1_move[1], a1_pay))
                self.a2.games_played.append((self.id, self.a2_move[1], a2_pay))

                self.a1.total_payoff += a1_pay
                self.a2.total_payoff += a2_pay

                return pay[1]
