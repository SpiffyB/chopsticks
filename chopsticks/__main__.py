'''
Created on 6 Sep 2019

@author: Tom
'''

import chopsticks.core as core
import sys
import argparse
from chopsticks.user_interface import Ui, Gui, CommandLine

def parse_arguments():
    parser = argparse.ArgumentParser(description="Chopticks Game")
    parser.add_argument("num_humans", help="Number of human players", type=int)
    parser.add_argument("num_bots", help="Number of bot players", type=int)
    parser.add_argument("num_hands", help="Number of hands that each player has", type=int)
    parser.add_argument("num_fingers", help="Number of fingers on each hand", type=int)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-g","--gui", help="Use the Graphical user interface")
    group.add_argument("-c","--cmd", help="Use the command line interface")

    return parser.parse_args()


def main():
    args = parse_arguments()
    g = core.Game(args.num_humans,
                  args.num_bots,
                  args.num_hands,
                  args.num_fingers,
                  Gui())
    g.play()


if __name__ == '__main__':
    main()