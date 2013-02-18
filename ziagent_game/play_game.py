import argparse as arg
import random as r

from ziagent_game.agents import Agent
from ziagent_game.settings import *



def setup_world(nagents=nagents):
    for x in range(nagents):
        Agent()
    #Return all Agent objects
    return Agent().__all__

def setup_game(ngames):
    for x in range(ngames):



def play_games(ngames):
    setup_games(ngames)




def main(nagents):
    setup_world(nagents)
    play_games(nagents/2)


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


if __name__ == '__main__':
    args = parse_args()
    main(args.agents)