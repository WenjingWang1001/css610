"""
CSS 610 | Spring 2013
=======================
Jacqueline Kazil
02/05/2013

Platform:
    Mac OSX 10.6.8
    
Software:
    python==2.7.3
    matplotlib==1.2.0
    numpy==1.6.2

To see options & how to run:
    $ python kazil_hw2_zi.py -h
"""

# Standard libraries
import argparse as arg
from collections import defaultdict
import random as r
import sys


# Supplement libraries
import numpy as np
import pylab
    

class Agent(object):
    """ 
    Zero-intelligence agents can be a buyer or seller. 
    Set the buyer type by passing Agent argument of 'b' or 's'.

    agent.intelligence is set to True or False. This is to determine 
    whether the agent is effected by the addition of intelligence

    agent.location is the location of the agent in a line (list) of agents
    """ 
    def __init__(self, agent_type, value=None, intelligence=True, location=0):
        if value:
            self.value = value
        else:
            self.value = r.randint(1,30)
        self.inventory = 1
        self.type = agent_type
        self.location = location
        self.intelligence = intelligence

def create_population(agent_type, nagents, plot=True, locations=None, zi=0):
    """
    Function to create a population of a certain type of agent.
    If locations, that means that 'sl' is active & neighbors are considered.
    """
    agents = [] 
    import sys 
    
    if locations:
        locations = range(0,locations)
        for i in range(nagents):

            location = r.choice(locations)
            locations.remove(location)
            neighbors = [location + 1, location - 1]
            neighbor_values = [a.value for a in agents if a.location in neighbors]
            
            if len(neighbor_values):
                values = sorted(neighbor_values)
                if agent_type == 'b':
                    value = values[-1] + 1
                else:  #agent_type == 's'
                    value = values[0] - 1
            else:
                value = r.randint(1,30)
            
            agent = Agent(agent_type, value, True, location)
            agents.append(agent)                
    else:
        agents = [Agent(agent_type) for i in range(nagents)]

    if zi:
        for i in range(zi):
            agents.append(Agent(agent_type, intelligence=False))
    
    sorted_agents = list(sorted([a.value for a in agents]))
    if agent_type == 'b':
        sorted_agents = list(reversed(sorted_agents))

    a_array = np.array(sorted_agents)

    if plot:
        x_agents = np.array((range(len(agents))))
        pylab.plot(x_agents, a_array)

    return agents

def adjust_value(agent, last_trade_price):
    """
    Adjusts agent value off of the last trade price.
    For sellers: If the price is higher, then they raise theirs by 1.
    For buyers: If the price is lower, then they lowers theirs by 1.
    """

    ltp = last_trade_price
    if ltp > agent.value:
        agent.value += 1
    elif ltp < agent.value:
        agent.value -= 1

    if agent.value < 0: 
        agent.value = 1

    return

def run(nagents, max_iterations, plot, intelligence=None, zi=0):
    """ 
    Creates a market of zero-intelligence traders.
    * First populations for buyers and sellers are created.
        * If the intelligence is set to 'sl', then buyers and sellers
            become aware of their neighbors prices when they set up shop.
        * During this, populations are plotted.
    * The market opens for 'max_iterations'. In each iteration...
        * A random buyer and seller is picked
        * If the buyer's value is greater than the seller's value a trade occurs.
        * Agent inventory is adjusted.
        * Trade is documented. 
        * Buyer and seller are removed from the eligible population.
    * Finally, the trades are plotted.
    """

    count = 0
    trade_price = None
    trades = {}

    if intelligence == 'sl':
        locations = ((nagents+zi)/2)
    else:
        locations = None

    # Establish agents
    if zi:
        buyers = create_population('b', nagents/2, plot, locations, zi/2)
        sellers = create_population('s', nagents/2, plot, locations, zi/2)
    else:
        buyers = create_population('b', nagents/2, plot, locations, zi)
        sellers = create_population('s', nagents/2, plot, locations, zi)

    b_values = sorted([b.value for b in buyers])
    s_values = sorted([s.value for s in sellers])

    mbuyers = [b for b in buyers]  #market buyers
    msellers = [s for s in sellers] #market sellers
    for i in range(max_iterations):

        count += 1

        if intelligence == 'av' and trade_price:
            [adjust_value(b,trade_price) for b in buyers if b.intelligence]
            [adjust_value(s,trade_price) for s in sellers if b.intelligence]

        b = r.choice(mbuyers)
        s = r.choice(msellers)

        if b.value > s.value:

            b.inventory -= 1
            s.inventory -= 1
            trade_price = r.randint(s.value,b.value)

            trades[count] = (s.value, b.value, trade_price)

            if b.inventory == 0:
                mbuyers.remove(b)
            if s.inventory == 0:
                msellers.remove(s)

    # Process output

    trade_values = sorted([v[2] for k,v in trades.iteritems()])
    trade_tally = defaultdict(int)
    for t in trade_values:
        trade_tally[t]+=1

    description = """
                    total population: %s
                    zi added: %s
                    
                    trade count: %s
                    average sale: %s
                    std: %s
                  """ % (nagents + zi,
                         zi,
                         #b_values,
                         #s_values,
                         #[(k,v) for k, v in trade_tally.iteritems()], #trade tally (price, occurances): %s
                         len(trades),
                         np.mean(trade_values),
                         round(np.std(trade_values, ddof=1), 2),
                         )

    if plot:
        # graph trades
        x = np.array((range(len(trades.keys()))))
        y = np.array([i[2] for i in trades.values()])
        pylab.plot(x, y)
        pylab.gca().set_position((.1, .3, .8, .6))
        pylab.ylabel('value')
        pylab.title('Zero-intelligence sample market')
        pylab.grid(True)
        pylab.figtext(0, 0, description)
        fig_location =  (str(intelligence).lower(), r.randint(1,1000)) 
        if zi:
            pylab.savefig('plots/%s/zi_%s.png' % fig_location, bbox_inches='tight')
        else:
            pylab.savefig('plots/%s/%s.png' % fig_location, bbox_inches='tight')

        
    else:
        print description


def parse_args():
    """ Create or parse commandline arguments. """
    description = """ 
                    Script creates zero-intelligence trading environment.
                    How to run:    
                        * Run w/o intelligence  
                            python zi.py
                        * Agents w/ neighbor intelligence during set up
                            python zi.py --intelligence sl
                            * Add zero-intelligence traders to spice thing up
                                python zi.py --intelligence sl -zi 50

                        * Agents adjust value based on previous trades
                            python zi.py --intelligence av
                            * Add zero-intelligence traders to spice thing up
                                python zi.py --intelligence av -zi 50

                    Plots will be saved to sub-folder.
                  """
    parser = arg.ArgumentParser(description=description)
    parser.add_argument('-a', type=int, dest='agents', default=50, 
                        help='Number of agents. Default: 50 = 25 buyers + 25 sellers.')
    parser.add_argument('-i', type=int, dest='max_iterations', default=10001, 
                        help='Number of max iterations. Default: 10000')
    parser.add_argument('--no-plot', dest='no_plot', action="store_false", 
                        help='Turn off graph.')
    help = """ 
            --intelligence sl
                sl == '(agents aware of) starting location'
                When agents find their position in the market they 
                decide their price with some intelligence. Each agent 
                can have two neighbors, which influence their price.
                If the agent arrives and it has no neighbors, it picks 
                a random price between 1 to 30. If the agent has one neighbor, 
                the agent beats their neighbor's price by 1 in order 
                to offer a better value. So, sellers will adjust 
                to 1 less than the lowest neighbor. Buyers will adjust to 
                1 more than the highest neighbor. 
            OR
            --intelligence av
                av == 'adjust value (during trading)'
                During the market, agents adjust price will adjust price.
                If it was more than the agent's value, then the agent's value
                increases by 1. If it was less, then it decreased by 1. 
            """
    parser.add_argument('--intelligence', dest='intelligence', default=None, help=help)
    help = """
            Add some # of zero-intelligence agents to the market.
            This only works when --intelligence is set. 

            If zi are added, then all agents assigned to -a are intelligent. 
            All agents assigned to zi are not. 

            So, -a 100 -zi 100, means there were will 200 agents in the market.
            100 buyers, 100 sellers.
            """
    parser.add_argument('-zi', type=int, default=0, dest='zi', help=help)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    run(args.agents, args.max_iterations, args.no_plot, args.intelligence, args.zi)
