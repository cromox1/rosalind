__author__ = 'cromox'

import networkx as nx

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

def dataset(dataALL, start, end):
    #grpnode = dataALL[start][0]
    #grpvrtc = dataALL[start][1]
    #print('INFO = ' + str(grpnode) + ' nodes / ' + str(grpvrtc) + ' edges')
    datagrp = dataALL[start + 1:end]
    edgedata = []
    for ii in range(len(datagrp)):
        edgedata = edgedata + [[int(datagrp[ii][0]),int(datagrp[ii][1]),int(datagrp[ii][2])]]
    return edgedata

def addEdgeWithWeight(Gx, vertexlist):
    from1 = int(vertexlist[0])
    to1 = int(vertexlist[1])
    weight1 = int(vertexlist[2])
    Gx.add_edge(from1, to1, weight=weight1)
    return Gx

def calccycleweight(Gx, firstnode, secondnode):
    try:
        weight1 = nx.dijkstra_path_length(Gx, secondnode, firstnode, weight='weight')
        weight2 = nx.dijkstra_path_length(Gx, firstnode, secondnode, weight='weight')
        if weight1 != 0 or None:
            print('WeightPath = ' + str(weight1 + weight2))
            return weight1 + weight2
        else:
            print('WeightPath = ' + str(-1))
            return -1
    except:
        print('WeightPath = ' + str(-1))
        return -1

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_cte.txt'
# pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
# fileinput = 'input23.txt'
filename = pathfile + fileinput

dataALL = inputfile(filename)
print(dataALL)

grpall = dataALL[0][0]
print('No of dataset = ' + grpall)

infolocatr = []
for i in range(len(dataALL)):
    if len(dataALL[i]) == 2:
        infolocatr.append(i)
    if i == len(dataALL) - 1:
        infolocatr.append(len(dataALL))
print(infolocatr)

resultx = []

for jj in infolocatr[:-1]:
    Gx = nx.DiGraph()
    start = jj
    end = infolocatr[infolocatr.index(jj) + 1]
    edgedataX = dataset(dataALL, start, end)
    nodescount = dataALL[start+1][0]

    for edgelist in edgedataX:
        addEdgeWithWeight(Gx, edgelist)

    firstedge = list(Gx.edges())[0]
    firstnode = firstedge[0]
    secondnode = firstedge[1]
    print('edge1 = ' + str(firstedge))
    print('node1 = ' + str(firstnode))
    print('node2 = ' + str(secondnode))

    cycleweightpath = calccycleweight(Gx, firstnode, secondnode)
    resultx.append(cycleweightpath)

print()
print('No of dataset = ' + grpall)
print()
print(*resultx)
