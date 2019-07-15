#!/usr/bin/env python3
from automaton import *
import sys


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
    prompt += '\n10. Extinction in Second-Order Conditioning'
    print(prompt)

    while True:
        experiment = input('\nEnter a number from 1 to 10 to see experiment:\n(enter exit to stop)\n')
        if experiment != ('exit' or 'Exit'):
            try:
                experiment = int(experiment)
                if experiment == 1:
                    first_order_condition()
                elif experiment == 2:
                    second_order_condition()
                elif experiment == 3:
                    latent_inhibition()
                elif experiment == 4:
                    extinction()
                elif experiment == 5:
                    silent_extinction()
                elif experiment == 6:
                    partial_reinforcement()
                elif experiment == 7:
                    simultaneous_condition()
                elif experiment == 8:
                    compound_condition()
                elif experiment == 9:
                    blocking()
                elif experiment == 10:
                    extinction_second_order_condition()
                else:
                    raise ValueError
            except ValueError:
                print(
                    'The program only accept a number from 1 to 10. Please enter a approriate input or enter \'exit\' to exit the program')
        else:
            print('Exit the program.')
            break
            sys.exit()


def first_order_condition():
    print('\nBeginning First Order Conditioning Experiment')
    cybernetic_automaton()
    print('_________________________________________End.\n')
    pass


def second_order_condition():
    print('Beginning Second Order Conditioning Experiment')
    pass


def latent_inhibition():
    print('Beginning Latent Inhibition Experiment')
    pass


def extinction():
    print('Beginning Extinction Experiment')
    pass


def silent_extinction():
    print('Beginning Silent Extinction Experiment')
    pass


def partial_reinforcement():
    print('Beginning Partial Reinforcement Experiment')
    pass


def simultaneous_condition():
    print('Beginning Simultaneous Conditioning Experiment')
    pass


def compound_condition():
    print('Beginning Compound Conditioning Experiment')


def blocking():
    print('Beginning Blocking Conditioning Experiment')


def extinction_second_order_condition():
    print('Beginning Extinction in Second Order Conditioning Experiment')


if __name__ == '__main__':
    interface()
