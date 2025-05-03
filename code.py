import time
import queue
import networkx as nx
import matplotlib.pyplot as plt

class Disjoint_set:

    def find(node, parent):
        if(node == parent[node]):
            return node
        
        parent[node] = find(parent[node],parent)
        return parent[node]
    
    def union(x, y,parent, rank ):
        if(x == y):
            return
        if(rank[x] == rank[y]):
            parent[x] = y
            rank[y] += 1
        elif (rank[x] < rank[y]):
            parent[x] = y
        else:
            parent[y] = x

        



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
v = int(input('Enter no. of vertex : '))
e = int(input('Enter no. of edges : '))
G.add_nodes_from(range(1,v+1))
for i in range(0,e):
    edges = input().split()
    e1 = int(edges[0])
    e2 = int(edges[1])
    G.add_edge(e1,e2)

pos = nx.spring_layout(G)
print('Graph created......',end='\n')

print('--------------- MENU ---------------')
print("1. BFS ")
print('1. Disjoint Set Union ')
print('2. Floyd-Warshall Algorithm')
print("3. Kosaraju's Algorithm ")
print('0. Exit')
print('------------------------------------')
print('Enter your option : ')
opt = int(input())
while(True):
    if(opt == 1):
        parent = []
        rank = []
        disjoint = Disjoint_set()
        visulize_graph('Graph Visualizer', G, pos)


pos = nx.spring_layout(G)


visulize_graph('Graph Visualizer', G, pos)
