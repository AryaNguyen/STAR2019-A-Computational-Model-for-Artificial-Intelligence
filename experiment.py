#!/usr/bin/env python3

from organism import *
import sys
import pandas as pd


def interface():
    prompt = 'Welcome to Experiment Model for a Computation Model for Artificial Intelligence\n'
    prompt += '\nList of all experiments:'
    prompt += '\n1. First-Order Conditioning'
    prompt += '\n2. Second-Order Conditioning'
    prompt += '\n3. Latent Inhibition'
    prompt += '\n4. Extinction'
    prompt += '\n5. Silent Extinction'
    prompt += '\n6. Partial Reinforcement'
    prompt += '\n7. Simultaneous Conditioning'
    prompt += '\n8. Compound Conditioning'
    prompt += '\n9. Blocking'
    prompt += '\n10. Extinction in Second-Order Conditioning\n'
    print(prompt)

    try:
        experiment = input('Enter a number from 1 to 10 to see experiment:\n')
        if experiment != 'exit':
            experiment = int(experiment)
            if experiment == 1:
                firstOrderConditioning()
            elif experiment == 2:
                secondOrderConditioning()
            elif experiment == 3:
                latentInhibition()
            elif experiment == 4:
                extinction()
            elif experiment == 5:
                silentExtinction()
            elif experiment == 6:
                partialReinforcement()
            elif experiment == 7:
                simultaneousConditioning()
            elif experiment == 8:
                compoundConditioning()
            elif experiment == 9:
                blocking()
            elif experiment == 10:
                extinctionSecondOrder()
            else:
                raise ValueError
        else:
            print('Exit the program.')
            sys.exit()
    except ValueError:
        print(
            'The program only accept a number from 1 to 10. Please enter a approriate input or enter \'exit\' to exit the program')


def firstOrderConditioning():
    print('Running First Order Conditioning Experiment')
    pass


def secondOrderConditioning():
    print('Running Second Order Conditioning Experiment')
    pass


def latentInhibition():
    print('Running Latent Inhibition Experiment')
    pass


def extinction():
    print('Running Extinction Experiment')
    pass


def silentExtinction():
    print('Running Silent Extinction Experiment')
    pass


def partialReinforcement():
    print('Running Partial Reinforcement Experiment')
    pass


def simultaneousConditioning():
    print('Running Simultaneous Conditioning Experiment')
    pass


def compoundConditioning():
    print('Running Compound Conditioning Experiment')


def blocking():
    print('Running Blocking Conditioning Experiment')


def extinctionSecondOrder():
    print('Running Extinction in Second Order Conditioning Experiment')


if __name__ == '__main__':
    interface()
