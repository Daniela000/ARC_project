import networkx as nx
from Node import Node
import random
#import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd


def summation(node, Nneighbour):
    summation = 0
    for neigbour in graph.neighbors(Nneighbour):
        if neigbour != node and neigbour != Nneighbour:
            summation += (cost/(graph.degree(neigbour)+1)) * neigbour.strategy - (cost/(graph.degree(node)+1)) * node.strategy
    return summation

def play():
    #calculate the fitness of each node

    for node in graph.nodes():
        for neigbour in graph[node]:
            if neigbour != node:
                node.fitness += (r/(graph.degree(neigbour) + 1) * ( ((cost/(graph.degree(neigbour)+1)) * neigbour.strategy - (cost/(graph.degree(node)+1)) * node.strategy) + summation(node, neigbour)))

    #compare the fitness of each node with a random node and update the stategy
    for node in graph.nodes():
        neighbour = random.choice(list(graph.neighbors(node)))

        if neighbour.fitness > node.fitness:
            node.update_strategy(neighbour)


if __name__ == "__main__":
    size = int(input("Indroduce the population size: "))
    cost = float(input ("Introduce coorperator's cost: ")) #the cost is equal for all coorperators?
    #minimum = input ("Introduce the minimum number of cooperators to win: ")
    r = float(input("Introduce the r factor: "))
    k = int(input("Indroduce the degree of each edge: "))

    graph = nx.barabasi_albert_graph(size,k)
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
        #node.strategy = random.choice([0, 1])


    fig = plt.figure()
    nx.draw(graph)
    plt.show()
    fig.savefig("graph.pdf")
    '''nx.draw(graph, with_labels=False)
    plt.show()'''

    num_coop = 0
    old_num_coop = None
    num_def = 0
    rows = []
    while old_num_coop != num_coop:
        strategy = [node.strategy for node in graph.nodes()]
        old_num_coop = num_coop
        num_coop = strategy.count(True)
        num_def = strategy.count(False)
        row = { 'n_coop' : num_coop, 'n_def' : num_def}
        rows.append(row)
        play()

    df = pd.DataFrame(rows)
    df.to_csv('simulation2.csv')

    fig = df.plot(y = ["n_coop", "n_def"]).get_figure()
    fig.savefig('simulation2.pdf')





        
