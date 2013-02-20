import argparse as arg
import random as r

from ziagent_game.agents import Agent
from ziagent_game.game import Game
from ziagent_game.common import *

def setup_world(nagents, memory):
    Agent.instances = []
    agents = []
    for x in range(0,nagents):
        agents.append(Agent(memory))
    return agents

def create_matchups(players):
    """ """
    l = players
    # Randomly shuffle agents
    r.shuffle(l)
    # Figure out how many agents = 1/2 the full list
    divider = len(l)/2
    # Create list of divided
    divided_players = [l[x:x+divider] for x in range(1, len(l), divider)]
    game_matches = zip(divided_players[0], divided_players[1])
    return game_matches

def play_games(agents):
    games = []
    matchups = create_matchups(agents)
    for m in matchups:
        games.append(Game(m))
    return games

def run(nagents, nruns, memory):
    agents = setup_world(nagents, memory)

    for x in range(nruns):
        games = play_games(agents)

    for a in agents:
        a.update_agent_values()