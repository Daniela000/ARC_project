import networkx as nx
from Node import Node
import random
import matplotlib as plt
import pandas as pd

def summation(node_y, node_x):
    summation = 0
    for node_i in graph.nodes():
        if node_i != node_x and node_i != node_y:
            summation += (cost/size) * node_i.strategy - (cost/size) * node_y.strategy
    return summation

def play():
    #calculate the fitness of each node
    for node_y in graph.nodes():
        for node_x in graph.nodes():
            if node_x != node_y:
                node_y.fitness += (risk/size * summation(node_y, node_x))

    #compare the fitness of each node with a random node and update the stategy
    for node_y in graph.nodes():
        neighbour = random.choice(list(graph.nodes()))
        while  neighbour == node_y :
            neighbour = random.choice(list(graph.nodes()))

        if neighbour.fitness > node_y.fitness:
            node_y.update_strategy(neighbour)


if __name__ == "__main__":
    size = int(input("Indroduce the population size: "))
    cost = float(input ("Introduce coorperator's cost: ")) #the cost is equal for all coorperators?
    #minimum = input ("Introduce the minimum number of cooperators to win: ")
    risk = float(input("Introduce the risk: "))

    graph = nx.Graph()

    #create nodes 50% are cooperators and 50% are defectors all the nodes have edges for all the nodes
    for i in range(size//2):
        graph.add_node(Node(True))
    for i in range(size - size//2):
        graph.add_node(Node(False))

    num_coop = 0
    num_def = 0
    rows = []
    for i in range(10):
        strategy = [node.strategy for node in graph.nodes()]
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