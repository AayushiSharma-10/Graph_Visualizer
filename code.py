import time
import queue
import networkx as nx
import matplotlib.pyplot as plt

def visulize_graph(title, G, pos):
    plt.figure()
    plt.title(title)
    for i in G:
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels= True, node_color=['g'])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)

G = nx.Graph()
G.add_edges_from([('A','B'), ('A','C'), ('A','D'),('B','C'),('B','E'), ('B','F'), ('C','E'),('C','D'),('C','F')])
pos = nx.spring_layout(G)

visulize_graph('Graph Visualizer', G, pos)