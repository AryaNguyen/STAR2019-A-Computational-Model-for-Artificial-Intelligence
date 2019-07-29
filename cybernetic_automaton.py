#!/usr/bin/env python3
""" An automaton object consists of states and transition 
This module comprises STATE object and Transition object
"""

import random
import sys
import os
import math
import pandas as pd
import numpy as np

SIGMA = {0: '',
         1: 'cs+',
         2: 'cs-',
         3: 'ucs+',
         4: 'ucs-'}

""" Object State
*** Attributes:
    ID:
    Next:
        
*** Methods: 
    
"""


class State:
    def __init__(self, state_id, next=None):
        self.__id = state_id
        self.__next = next
        self.__stimulus = None
        self.__transition = None
        self.__reward = False
        self.__punishment = False

    def __str__(self):
        return 'State {}'.format(str(self.__id))

    """ create new transition which will determine the next state
    """
    def add_transition(self, stimulus, transition):
        # first state in the list of states
        self.__stimulus = stimulus
        self.__transition = transition

    def get_next_state(self):
        return self.__next

    def is_initial(self):
        return self.__id == 0

    def is_last(self):
        return self.__id == Q.index(Q[-1])

    def is_reward(self):
        return self.__reward is True

    def is_punishment(self):
        return self.__punishment is True


""" Object Transition 
____ Attributes:
    
    
____Methods: 
    
"""


class Transition:
    def __init__(self, current_state, next_state, epsilon=None, temporary=False):
        self.__current = current_state
        self.__next = next_state
        self.__temporary = temporary

        self.__epsilon = epsilon
        self.__C = None  # Confidence
        self.__E = None  # Expectation

    def __str__(self):
        return 'Transition from {} --> {}'.format(self.__current, self.__next)

    def get_current(self):
        return self.__current

    def get_next(self):
        return self.__next

    def get_confidence(self):
        return self.__C

    def get_expectation(self):
        return self.__E

    def set_confidence(self, c):
        self.__C = c

    def set_expectation(self, e):
        self.__E = e

    def is_temporary(self):
        return self.__temporary is True

    def generate_output(self):
        pass


class Stimulus:
    def __init__(self, symbol):
        self.__symbol = symbol

    def __str__(self):
        return 'Stimulus: {}'.format(self.__symbol)

    def __getitem__(self, item):
        """
        """
        global SIGMA
        for num, symbol in enumerate(SIGMA):
            if item == symbol:
                return num
        return None


if __name__ == '__main__':
    print('Example of State and Transition object:')
    Q = []
    q = None
    list_states = np.array([0, 1, 2])
    for i in list_states:
        q = State(i)
        Q.append(q)
    print(Q[0])
    t = Transition(Q[0], Q[1])
    print(t)








