from automaton import *
import pandas as pd


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

    """
    def step1(self):
        self.__c = self.__Q[0]
        self.__ql = self.__Q[0]
        self.__al = self.__Epsilon
        self.__ol = self.__Epsilon

        self.step2()

    def step2(self):
        if True:
            if True:
                if True:
                    pass
                self.__ql = self.__c
                self.__c = c.transition(self.__Epsilon)
            self.__qa = self.__c
            self.__al = self.__Epsilon
            self.__ol = self.__Epsilon

    def step3(self):
        file_input = 'cs+'
    """


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