""" This module build an Cybernetic Automaton from State and Transiiton object (from Automaton module)

The Cybernetic Automaton use for ... 
"""

from automaton import *
import pandas as pd


""" A Cybernetic Automaton consists of ... steps
"""


class CyberneticAutomaton:
    def __init__(self, model_parameter, sigma, delta):
        self.__model_parameter = model_parameter
        self.__SIGMA = sigma  # input alphabet
        self.__DELTA = delta  # output alphabet

        self.__Q = []  # states
        self.__R = None  # reward states
        self.__P = None  # punishment states
        self.__Epsilon = None

        self.__c = None
        self.__ql = None
        self.__al = None
        self.__ol = None
        self.__qa = None

    def __str__(self):
        pass

    def step1(self):
        q0 = self.__Q[0]
        self.__c = q0
        self.__ql = q0
        self.__al = self.__Epsilon
        self.__ol = self.__Epsilon

        self.step2()

    def step2(self):
        if True:
            if True:
                if True:
                    pass
                self.__ql = self.__c
                self.__c = self.__c.transition(self.__Epsilon)
            self.__qa = self.__c
            self.__al = self.__Epsilon
            self.__ol = self.__Epsilon

    def step3(self):
        file_input = 'cs+'

    def step4(self):
        pass

    def step5(self):
        self.create_transition()

    def step6(self):
        pass

    def step7(self):
        pass

    def step8(self):
        pass

    def step9(self):
        pass

    def step10(self):
        self.update_expectation()

    def step11(self):
        if self.__c in self.__R:
            self.apply_reward()
        elif self.__c in self.__P:
            self.apply_punishment()
        else:
            self.apply_conditioning()

    def step12(self):
        self.step2()

    def create_transition(self):
        pass

    def update_expectation(self):
        pass

    def apply_reward(self):
        pass

    def apply_punishment(self):
        pass

    def apply_conditioning(self):
        pass

    def update_conditioning(self):
        pass


if __name__ == '__main__':
    model = CyberneticAutomaton(1, 1, 1)