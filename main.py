import matplotlib.pyplot as plt
from agent import Agent
import random

plotRealTime = True
Nt = 500
min_pos = 5
max_pos = 15
num_agents = 20
L = 20


# Creating agents 
agents = [Agent(random.randint(min_pos, max_pos), random.randint(min_pos, max_pos)) for i in range(num_agents)]

stubborn_agent = Agent(10, 5)

fig, ax = plt.subplots()
for i in range(Nt):

    x = [agent.x % L for agent in agents]
    y = [agent.y % L for agent in agents]

    for agent in agents:
        agent.move_with_stubborn_agent(stubborn_agent)

    if plotRealTime or (i == Nt-1):
        plt.cla()
        plt.scatter(x, y, s=10, c='k')
        ax.scatter(10, 5, s=10, c='y')
        ax.set(xlim=(0, L), ylim=(0, L))
        ax.set_aspect('equal')
        plt.pause(0.01)
        

    for agent in agents:
        agent.move()


plt.show()
