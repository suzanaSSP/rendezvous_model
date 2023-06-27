import numpy as np
import random
from typing import List
import math


# Simulation parameters
dt           = 0.1     # time step
a            = 10      # agent is visible to other agent in time a
L            = 2000    # Size of box
N            = 26
num_agents   = 3

# Deal with NaN bugs
np.seterr(divide='ignore', invalid='ignore')

class Agent:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = np.array([self.x,self.y])

        self.change_x = 0
        self.change_y = 0

        self.connections = None

    def find_connections(self, agents):
        num_of_connection_agent = random.randint(0,(num_agents - 1))   

        # Find random function that picks a random item in a list and use it in this list comprehension
        self.connections = [random.choice(agents) for _ in range(num_of_connection_agent)]
    
    def find_distances(self, agents):
        self.find_connections(agents)

        for agent in self.connections:
            self.change_x += (agent.x - self.x)
            #self.change_y += (agent.y - self.y)
    
    def move(self):
        new_x = self.x + (self.change_x * dt)
        #new_y = self.y + (self.change_y * dt)

        self.x = new_x
        #self.y = new_y

    def move_with_stubborn_agent(self, stubbron_agent):
        self.change_x = stubbron_agent.x - self.x


