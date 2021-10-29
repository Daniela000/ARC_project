import networkx as nx
from Node import Node
import random
#import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd


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

        value = node.fitness
        node.fitness = value/len(graph[node])

    #compare the fitness of each node with a random node and update the stategy
    for node in graph.nodes():
        neighbour = random.choice(list(graph.neighbors(node)))

        if neighbour.fitness > node.fitness:
            node.update_strategy(neighbour)


if __name__ == "__main__":

    size = 10000
    #cost = 1
    #r = 5
    k = 4

    graphs = []
    for _ in range(10):
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
    
        graphs.append(graph)

    

  
    for graph in graphs:
        num_coop = 0
        old_num_coop = None
        num_def = 0
        rows = []

        for i in range(50):
            strategy = [node.strategy for node in graph.nodes()]
            old_num_coop = num_coop
            num_coop = strategy.count(True)
            num_def = strategy.count(False)
            row = { 'n_coop' : num_coop, 'n_def' : num_def}
            rows.append(row)
            play("SH")

        df = pd.DataFrame(rows)
        df.to_csv('csv/simulation'+str(graphs.index(graph))+'.csv')

        fig = df.plot(y = ["n_coop", "n_def"]).get_figure()
        fig.savefig('images/simulation'+str(graphs.index(graph))+'.pdf')