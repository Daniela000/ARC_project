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

def play(S,T):
    R = 1
    #if game=="PD":
        #T = 1.1
        #S = -0.2
    #elif game=="SH":
        #T = 0.9
        #S = -0.9
    #else:
        #S = 0.5
        #T = 1.1


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

    size = 1000
    k = size - 1

    heat = []
    y_label = []
    x_label = ['{:3.1f}'.format(T*0.1) for T in range(0,21)]
    for i in range(21):
        heat.append([])
        for _ in range(21):
            heat[i].append(0)
    for a in range(10):
        graph = nx.complete_graph(size)
        nx.relabel_nodes(graph, mapping=Node, copy=False)
        x=0
        for S in range(10,-11,-1):
            S *=0.1
            if a == 0:
                y_label.append('{:3.1f}'.format(S))
            #print(S)
            aux=0
            #heat.append([])
            for T in range(0,21):
                T*=0.1
                #print(T)

                nodes = list(graph.nodes())
                i = size // 2
                while i > 0:
                    node = random.choice(nodes)
                    node.strategy = True
                    node.fitness = 0
                    nodes.remove(node)
                    i-=1
                while nodes !=[]:
                    node = random.choice(nodes)
                    node.strategy = False
                    node.fitness = 0
                    nodes.remove(node)

            #fig = plt.figure()
            #nx.draw(graph)
            #plt.show()
        #fig.savefig("graph.pdf")

                num_coop = 0
                old_num_coop = None
                num_def = 0
            #defe = []
            #coop = []
            #rows = []
                row = [[],[]]
                old_graph = None
                cont = 0
                for i in range(50):
                    if old_num_coop == num_coop:
                        cont += 1
                        if cont == 2:
                            break
                #rows.append([])
                #defe.append([])
                #coop_sh.append([])
                    strategy = [node.strategy for node in graph.nodes()]
                    old_num_coop = num_coop
                    num_coop = strategy.count(True)
                    #num_def = strategy.count(False)
                #defe_sh[i].append(num_def)
                #coop_sh[i].append(num_coop)
                    play(S,T)
                print("S",S)
                print("T",T)
                print("A",a)
                print("coops",num_coop)
                #print("x " + str(x) + " aux " + str(aux))
                heat[x][aux] += (num_coop/size)*10
                #heat[x].append((num_coop/size)*100)
                aux += 1
            x+=1
        #df = pd.DataFrame(rows)
        #df.to_csv('homogenous_sim/simulation'+str(x)+'.csv')

        #fig = df.plot(y = ["n_coop", "n_def"]).get_figure()
        #fig.savefig('homogenous_sim/simulation'+str(x)+'.pdf')

new_rows = []
#coop_sh = [value for value in coop_sh if value != []]
#defe_sh = [value for value in defe_sh if value != []]

#print(rows)
#for game in rows:
    #print(game)
    #average_coop = sum(game[0])/10
    #average_def = sum(game[1])/10
    #new_row = { 'avg_coop' : average_coop, 'avg_def' : average_def}
    #new_rows.append(new_row)
#rows = {'avg_coop' : coop_sh + coop_pd, 'avg_def': defe_sh  + defe_pd}
#print(rows)
#new_row = {'avg_coop' : [], 'avg_def' : []}
#for line in rows['avg_coop']:
    #new = sum(line)/len(line)
    #new_row['avg_coop'].append(new)
#for line in rows['avg_def']:
    #new = sum(line)/len(line)
    #new_row['avg_def'].append(new)
#print(new_row)
#df = pd.DataFrame(new_row)
#df.to_csv('homogenous_sim/avg.csv')

#fig = df.plot(y = ["avg_coop", "avg_def"]).get_figure()
#fig.savefig('homogenous_sim/avg.pdf')

print(heat)
#ax = sns.heatmap(heat, vmin =0, vmax=100, xticklabels=x_label, yticklabels=y_label,cmap = "Spectral")
#fig = ax.get_figure()
#fig.savefig('homogeneous_sim/heatmap.pdf')
fig = plt.figure()
plt.rcParams["axes.grid"] = False
plt.xlabel('T')
plt.xlabel('S')
img = plt.imshow(heat, cmap='jet', interpolation="spline16", vmin =0, vmax=100, extent = [0,2,-1,1])

#fig.colorbar(img)
fig.savefig('homogeneous_sim/heatmap.pdf')
