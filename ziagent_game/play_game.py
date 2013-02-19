import argparse as arg
import random as r

from ziagent_game.agents import Agent
from ziagent_game.game import Game
from ziagent_game.common import *



def setup_world(nagents=nagents):
    for x in range(nagents):
        Agent()
    #Return all Agent objects
    return Agent().instances

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
    matchups = create_matchups(agents.keys())
    for m in matchups:
        game_agents = (agents[m[0]], agents[m[1]])
        Game(game_agents)
    return Game.instances

def parse_args():
    """ 
    Create or parse commandline arguments.
    """
    description = """ 
                    # TODO
                  """
    parser = arg.ArgumentParser(description=description)
    parser.add_argument('-a', type=int, dest='agents', default=nagents, 
                        help='Number of agents.')
    return parser.parse_args()

def main(nagents):
    agents = setup_world(nagents)
    games = play_games(agents)
    print games

if __name__ == '__main__':
    args = parse_args()
    main(args.agents)