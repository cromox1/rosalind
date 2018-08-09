__author__ = 'cromox'

import networkx as nx

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

def addEdgeWithWeight(Gx, vertexlist):
    from1 = int(vertexlist[0])
    to1 = int(vertexlist[1])
    weight1 = int(vertexlist[2])
    Gx.add_edge(from1, to1, weight=weight1)

def lessWeightDijkstra(Gx, nodescount):
    print("Nodes of graph: " + str(Gx.nodes()))
    print("Edges of graph: " + str(Gx.edges()))
    dists = nx.shortest_path_length(Gx, 1, weight='weight')
    nodeexist = list(Gx.nodes())
    nodeexist.sort()
    print('No_of_Nodes_Exist = ' + str(len(nodeexist)))
    # print('Node_Exist = ' + str(nodeexist))
    nodereqd = list(range(1,nodescount+1))
    nodereqd.sort()
    print('No_of_Nodes_Reqrd = ' + str(len(nodereqd)))
    # print('Node_Reqrd = ' + str(nodereqd))
    print()
    for node in nodereqd:
        print(dists.get(node, 'x'),end=' ')
    print()

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_bf.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input22.txt'
filename = pathfile + fileinput

dataALL = inputfile(filename)
print(dataALL)

nodeall = dataALL[0][0]
edgeall = dataALL[0][1]
print('No of nodes = ' + nodeall)
print('No of edges = ' + edgeall)

edgedatalist = []
for i in range(1, len(dataALL)):
    edgedatalist.append(dataALL[i])
print('EdgeDataList = ' + str(edgedatalist))

Gx = nx.DiGraph()

for vertexlist in edgedatalist:
    # print(datavertex)
    addEdgeWithWeight(Gx, vertexlist)

lessWeightDijkstra(Gx, int(nodeall))
