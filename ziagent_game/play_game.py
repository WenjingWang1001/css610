import argparse as args
import random as r

from ziagent_game.agents import Agent
from ziagent_game.game import Game
from ziagent_game.common import *


def setup_world(nagents, memory, rut_percentage):
    'Empties agent instances & creates new agents as specified.'
    Agent.instances = []
    agents = []
    for x in range(0,nagents):
        agents.append(Agent(memory, rut_percentage))
    return agents

def create_matchups(players):
    'Creates matchups for a game by randomizing players.'
    l = players
    # Randomly shuffle agents
    r.shuffle(l)
    # Figure out how many agents = 1/2 the full list
    divider = len(l)/2
    # Create list of divided
    divided_players = [l[x:x+divider] for x in range(1, len(l), divider)]
    game_matches = zip(divided_players[0], divided_players[1])
    return game_matches

def play_games(agents, time):
    'Plays games for one tick.'
    games = []
    matchups = create_matchups(agents)
    for m in matchups:
        games.append(Game(m, time))
    return games

def run(nagents, nruns, memory, rut_percentage=100):
    """
    This is main function of the model & executes the following:
    * Sets up a new world with nagents that have a memory of memory. 
    * Plays nruns games.

    example: 100 agents, play 10 games, and have a memory of 2 games
    run(100, 10, 2)
    """
    time = TimeTick(0, nruns)
    agents = setup_world(nagents, memory, rut_percentage)
    
    while time.end > time.current:
        time.inc_time()
        games = play_games(agents, time.current)

    for a in agents:
        a.update_agent_values()