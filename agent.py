import numpy as np
import random

class Agent:
    dt = 0.1
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = np.array([self.x,self.y])

        self.change_x = 0
        self.change_y = 0

        self.connections = []

    def create_connections(self, agents, num_agents):
        # List of agents that are not self and are not connections already
        foreigners = [other_agent for other_agent in agents if other_agent is not self and other_agent not in self.connections]
    
        if len(foreigners) == 0:
            return None
        
        # How many agents I want to be connected with, minus those I'm already connection with
        num_of_connection = abs(random.randint(1, min(6, (num_agents//3))) - len(self.connections)) #why absolute value? might cause problems -hannah
        
        self.connections += [random.choice(foreigners) for _ in range(num_of_connection)]

        for agent in self.connections:
            if self not in agent.connections:
                agent.connections.append(self)
          
    def find_distances(self):
        for agent in self.connections:
            self.change_x += (agent.x - self.x)
            #self.change_y += (agent.y - self.y)

    def move(self):
        new_x = self.x + (self.change_x * self.dt)
        self.x = new_x
        self.change_x = 0

    def move_with_stubborn_agent(self, stubbron_agent): 
        self.change_x = stubbron_agent.x - self.x

