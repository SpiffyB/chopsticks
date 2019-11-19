'''
Created on 6 Sep 2019

@author: Tom
'''

import chopsticks.core as core
import sys


def main():
    g = core.Game(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
    g.play()


if __name__ == '__main__':
    main()