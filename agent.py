import numpy as np
import random
from typing import List
import math


# Simulation parameters
dt           = 0.1     # time step
a            = 10      # agent is visible to other agent in time a
L            = 2000    # Size of box
N            = 26
num_agents   = 5

# Deal with NaN bugs
np.seterr(divide='ignore', invalid='ignore')

class Agent:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = np.array([self.x,self.y])

        self.change_x = 0
        self.change_y = 0

        self.connections = []

    def find_connections(self, agents):
        # List of agents that are not self and are not connections already
        foreigners = [other_agent for other_agent in agents if other_agent is not self and other_agent not in self.connections]
        # How many agents I want to be connected with, minus those I'm already connection with
        num_of_connection = (round(random.randint(1, len(foreigners)), 0) ) - len(self.connections)
        
        self.connections = [random.choice(foreigners) for _ in range(num_of_connection)]

        for agent in self.connections:
            if self not in agent.connections:
                agent.connections.append(self) 
        
    
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


