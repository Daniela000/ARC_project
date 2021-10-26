import random
import math
import numpy as np

class Node:

    def __init__(self, strategy, fitness = 0):
        self.strategy = strategy
        self.fitness = fitness
    
    def fermi_integral(self,fx,fy, b):
        return 1 / (1 + np.exp(-b*(fy - fx)))

    def update_strategy(self, neighbour):
        p = self.fermi_integral(self.fitness,neighbour.strategy, 10.0)

        if(random.random() < p):
            self.strategy = neighbour.strategy
                




