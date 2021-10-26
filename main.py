import networkx as nx
from Node import Node
import random
import pandas as pd
import matplotlib.pyplot as plt

def summation(node_y, node_x):
    summation = 0
    for node_i in graph.neighbors(node_x):
        if node_i != node_y:
            summation += (cost/(k+1)) * node_i.strategy - (cost/(k+1)) * node_y.strategy
    return summation

def play():
    #calculate the fitness of each node
    for node_y in graph.nodes():
        for node_x in graph[node]:
            node_y.fitness += (r/(k+1)) * ( ((cost/(k+1)) * node_x.strategy - (cost/(k+1)) * node_y.strategy) + summation(node_y, node_x))

    #compare the fitness of each node with a random node and update the stategy
    for node_y in graph.nodes():
        neighbour = random.choice(list(graph.neighbors(node_y)))

        if neighbour.fitness > node_y.fitness:
            node_y.update_strategy(neighbour)


if __name__ == "__main__":
    size = int(input("Indroduce the population size: "))
    cost = float(input ("Introduce coorperator's cost: ")) #the cost is equal for all coorperators?
    r = float(input("Introduce the r factor: "))
    k = int(input("Indroduce the degree of each edge: "))

    graph = nx.random_regular_graph(k, size)
    nx.relabel_nodes(graph, mapping=Node, copy=False)

    nodes = list(graph.nodes())
    i = size // 2
    while i > 0:
        node = random.choice(nodes)
        node.strategy = True
        nodes.remove(node)
        i-=1
    while nodes !=[]:
        node = random.choice(nodes)
        node.strategy = False
        nodes.remove(node)

    fig = plt.figure()
    nx.draw(graph)
    plt.show()
    fig.savefig("graph.pdf")

    num_coop = 0
    old_num_coop = None
    num_def = 0
    rows = []
    while num_coop != old_num_coop:
        strategy = [node.strategy for node in graph.nodes()]
        old_num_coop = num_coop
        num_coop = strategy.count(True)
        num_def = strategy.count(False)
        row = { 'n_coop' : num_coop, 'n_def' : num_def}
        rows.append(row)
        play()

    df = pd.DataFrame(rows)
    df.to_csv('simulation.csv')

    fig = df.plot(y = ["n_coop", "n_def"]).get_figure()
    fig.savefig('simulation.pdf')





        


        

    


    #while old_graph != graph:
        #for  neigbour of i:
            #if payoff_neigbour > payoff_i:
                #strategy_i = stategy_neigbour