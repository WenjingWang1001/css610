import random as r
from collections import deque


class Agent(object):
    "Object class for agents."
    __all__ = deque()
    def __init__(self, agent_id=None):
        self.__class__.__all__.append(self)
        self.id = self.id_check(agent_id)
        self.move = r.randint(0,1)
        self.previous_moves = deque()

    def id_check(self, agent_id):
        try:
            agents_ids = [a.id for a in Agent.__all__]
        except AttributeError, e:
            agent_ids = []

        if agent_id in agent_ids:
            raise Exception("Agent_id already taken.")
        elif agent_id not in agent_ids:
            return agent_id
        else:
            last_agent_id = sorted(agent_ids)[-1]
            return last_agent_id + 1    

    def generate_move(self):
        previous_move = self.move
        self.previous_moves.append(previous_move)
        
        self.move = random.randint(0,1)