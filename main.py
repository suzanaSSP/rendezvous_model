import matplotlib.pyplot as plt
from agent import Agent
import random

plotRealTime = True
Nt = 500
min_pos = 40
max_pos = 80
num_agents = 10
L = 100

def main():
    # Creating agents 
    agents = [Agent(random.randint(min_pos, max_pos), random.randint(min_pos, max_pos)) for i in range(num_agents)]

    # Creating connections
    for agent in agents:
        agent.create_connections(agents, num_agents)

    fig, ax = plt.subplots()

    for i in range(Nt):

        x = [agent.x for agent in agents]
        y = [agent.y for agent in agents]

        for agent in agents:
            agent.find_distances() 
            
        if plotRealTime or (i == Nt-1):
            plt.cla()
            plt.scatter(x, y, s=10, c='k')
            ax.set(xlim=(0, L), ylim=(0, L))
            ax.set_aspect('equal')
            plt.pause(0.1)
            
        for agent in agents:
            agent.move()


    plt.show()

if __name__ == '__main__':
    main()
