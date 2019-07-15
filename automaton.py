#!/usr/bin/env python3
import random
import sys
import os
import math
import pandas
import numpy
from matplotlib import *

SIGMA = {0: '',
         1: 'cs+',
         2: 'cs-',
         3: 'ucs+',
         4: 'ucs-'}


class State:
    def __init__(self, state_id, next=None):
        self.__id = state_id
        self.__next = next
        self.__reward = False
        self.__punishment = False
        self.__transition = None

    def __str__(self):
        return str(self.__id)

    """ create new transition which will determine the next state
    """
    def add_transition(self, Input):
        if not self.is_initial() and not self.is_initial():
            self.__transition = Transition(Input, previous=0, next_state=0)
        # last state in the list of states
        elif not self.is_initial() and self.is_initial():
            self.__transition = Transition(Input, previous=0, next_state=0)
        # first state in the list of states
        else:
            self.__transition = Transition(Input)

    def get_next_state(self):
        return self.__next

    def is_initial(self):
        return self.__id == 0

    def is_last(self):
        last_state = Q[-1]
        return self.__id == Q.index(last_state)

    def is_reward(self):
        return self.__reward is True

    def is_punishment(self):
        return self.__punishment is True


class Transition:
    def __int__(self, Input, previous=None, next_state=None, epsilon=None, temporary=False):
        self.__input = Input
        self.__previous = previous
        self.__C = None
        self.__E = None
        self.__temporary = temporary
        self.__epsilon = epsilon

        self.__C = None  # Confidence
        self.__E = None  # Expectation

    def __str__(self):
        return '{} --> {}'.format(self.__previous, self.__next)

    def get_previous(self):
        return self.__previous

    def get_next(self):
        return self.__next

    def get_confidence(self):
        pass

    def get_expectation(self):
        pass

    def set_confidence(self):
        pass

    def set_expectation(self):
        pass

    def is_temporary(self):
        return self.__temporary is True

    def generate_output(self):
        pass


def get_symbol_index(s):
    global SIGMA
    for num, symbol in enumerate(SIGMA):
        if s == symbol:
            return num
    return None


if __name__ == '__main__':
    Q = []
    q = None
    list_states = numpy.array([0, 1, 2])
    for i in list_states:
        print(i)
        q = State(i)
        Q.append(q)






