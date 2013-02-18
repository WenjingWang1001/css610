import argparse as arg

from ziagent_game.agents import Agent
from ziagent_game.settings import *


def setup_world(nagents=nagents):
    for x in range(nagents):
        Agent(x)
    print

def main(nagents):
    setup_world()

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