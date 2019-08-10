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

"""
SIGMA = {0: '',
         1: 'ucs+',
         2: 'ucs-',
         3: 'cs+',
         4: 'cs-'}
Q = []
SIGMA = ()
DELTA = ()
"""

class State:
    """
    """
    def __init__(self, name, next_state=None):
        self.__name = name
        self.__next_state = next

        self.__stimulus = None
        self.__transition = None
        self.__reward = False
        self.__punishment = False

    def __str__(self):
        return 'State {}'.format(str(self.__name))

    """ create new transition which will determine the next state
    """
    def add_transition(self, stimulus, transition):
        # first state in the list of states
        self.__stimulus = stimulus
        self.__transition = transition

    def get_next_state(self):
        return self.__next_state

    def is_initial(self):
        return self is Q[0]

    def is_terminal(self):
        return self is Q[-1]

    def is_reward(self):
        return self.__reward

    def is_punishment(self):
        return self.__punishment


class Transition:
    """
    """
    def __init__(self, enter_state, exit_state, stimuli, confidence=None, is_temporary=False):
        self.__enter_state = enter_state
        self.__exit_state = exit_state
        self.__stimuli = stimuli
        self.__C = confidence
        self.__is_temporary = is_temporary

    def __str__(self):
        return 'Transition from {} --> {} at event {}'.format(self.__enter_state, self.__exit_state, self.__stimuli)

    def get_confidence(self):
        return self.__C

    def get_expectation(self):
        return self.__E

    def set_confidence(self, c):
        self.__C = c

    def is_temporary(self):
        return self.__temporary is True

    def generate_output(self):
        pass


class Stimuli:
    """
    """
    def __init__(self, symbol, num):
        self.__symbol = symbol
        self.__id = num

    def __str__(self):
        return 'Stimuli: {}'.format(self.__symbol)

    def __getitem__(self, item):
        global DELTA
        for num, symbol in enumerate(DELTA):
            if item == symbol:
                return num
        return None


class CyberneticAutomaton:
    def __init__(self, model_parameter, states, sigma, delta, R=0, P=0):
        self.__model_parameter = model_parameter
        self.__Q = []  # states
        for num in range(int(states)):
            self.__Q.append(State(num))


        self.__SIGMA = sigma  # input alphabet
        self.__DELTA = delta  # output alphabet
        self.__transitions = []

        self.__R = R # reward states
        self.__P = P  # punishment states
        self.__Epsilon = None

    def __str__(self):
        string = 'Cybernetic Automaton Information:'
        string += '\n\nModel Parameter: {}'.format(self.__model_parameter)
        string += '\n{} states:'.format(len(self.__Q))
        for q in self.__Q:
            string += '\n'
            string += str(q)
        string += '\n{} input alphabets'.format(self.__SIGMA)
        string += '\n{} output alphabets'.format(self.__DELTA)
        return string

    def add_state(self, state):
        self.__Q.append(state)

    def add_transition(self, start, end, stimuli, confidence=None):
        transition = Transition(start, end, stimuli, confidence)
        self.__transitions.append(transition)


if __name__ == '__main__':
    """
    #Example of State and Transition object:
    Q = []
    q = None
    list_states = np.array([0, 1, 2])
    for i in list_states:
        q = State(i)
        Q.append(q)
    print(Q[0])
    t = Transition(Q[0], Q[1])
    print(t)
    """

    # Import input sequence
    input_sequence = pd.read_csv('input.csv').iloc[:, -1]

    # get the parameters from the input_sequence --> create cybernetic model
    try:
        model_parameter = list(map(float, input_sequence[0:7].tolist()))
        states = int(input_sequence[7])
        sigma = int(input_sequence[8])
        delta = int(input_sequence[9])
        reward = int(input_sequence[10])
        punishment = int(input_sequence[11])

        ca = CyberneticAutomaton(model_parameter, states, sigma, delta)
        #print(ca)
    except ValueError:
        print(-1)

    # Create transitions from input sequence line 12 to the end
    transitions = []
    row_count = sum(1 for row in input_sequence)  # count the number of row in the input_sequence
    for i in range(12, row_count):
        list_arguments = input_sequence[i].split()
        t = Transition(list_arguments[0], list_arguments[1], list_arguments[2], list_arguments[3])
        #print(t)

    # Build the model

    print('\n')
    # Get stimuli input
    stimuli = input('Enter stimuli:\n')




















