#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Use to plot graphs
"""
import matplotlib.pyplot as plt

class Graph():
    """A graph
    
    ----------
    Attributes
    ----------
    *args: 
        list of tuple of x and y [(x, y), (x1, y1)]
        
    title: string
        title of the graph
        
    file_name: string
        save the figures to the file
        
    grid: boolean (default=True) 
        if True, the graphs will have grid
    
    
    ----------
    Methods
    ----------
    plot: plot graph and save the figure
    
    """
    def __init__(self, args, title, file_name, grid=True, label=None, linestyle=None):
       self.args = args
       self.title = title
       self.file_name = file_name
       self.grid = True
       self.label = label
       self.linestyle = linestyle
    
    def plot_save(self):
        for index, value in enumerate(self.args):
            if (self.linestyle and self.label) is None:
                plt.plot(value[0], value[1])
            else:
                plt.plot(value[0], value[1], label=self.label[index], linestyle=self.linestyle[index])
        plt.title(self.title, y=-0.3, fontdict={'fontsize':15})
        plt.xlabel('Trial batch')
        plt.ylabel('Responses')
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0,x1 + 1,
                  y0,y1 + 1))
        plt.grid(True)
        plt.savefig(self.file_name, dpi=300, bbox_inches="tight")
        plt.show()

if __name__ == '__main__':
    pass

