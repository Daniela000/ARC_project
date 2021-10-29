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

def play(game):
    R = 1
    if game=="PD":
        T = 1.1
        S = -0.2
    elif game=="SH":
        T = 0.9
        S = -0.9
    else:
        S = 0.5
        T = 1.1


    #calculate the fitness of each node
    for node in graph.nodes():
        s_node = node.strategy
        for neighbour in graph[node]:
            s_neighbour = neighbour.strategy
            #both coop
            if(s_node==1 and s_neighbour==1):
                node.fitness+=R 
            #coop vs def
            elif(s_node==1 and s_neighbour==0):
                node.fitness+=S 
            ##def vs coop
            elif(s_node==0 and s_neighbour==1):
                node.fitness+=T 
            #both def : do nothing

    #compare the fitness of each node with a random node and update the stategy
    for node_y in graph.nodes():
        neighbour = random.choice(list(graph.neighbors(node_y)))

        if neighbour.fitness > node_y.fitness:
            node_y.update_strategy(neighbour)


if __name__ == "__main__":
    #size = int(input("Indroduce the population size: "))
    #cost = float(input ("Introduce coorperator's cost: ")) #the cost is equal for all coorperators?
    #r = float(input("Introduce the r factor: "))
    #k = int(input("Indroduce the degree of each edge: "))

    size = 100
    k = 4
    for x in range(10):
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

        #fig = plt.figure()
        #nx.draw(graph)
        #plt.show()
    #fig.savefig("graph.pdf")

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
            play("SH")

        df = pd.DataFrame(rows)
        df.to_csv('homogenous_sim/simulation'+str(x)+'.csv')

        fig = df.plot(y = ["n_coop", "n_def"]).get_figure()
        fig.savefig('homogenous_sim/simulation'+str(x)+'.pdf')





        


        

    