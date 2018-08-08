__author__ = 'cromox'

import networkx as nx

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

def dataset(dataALL, start, end):
    #grpnode = dataALL[start + 1][0]
    #grpvrtc = dataALL[start + 1][1]
    #print('INFO = ' + str(grpnode) + ' nodes / ' + str(grpvrtc) + ' edges')
    datagrp = dataALL[start + 2:end]
    edgedata = []
    for ii in range(len(datagrp)):
        edgedata = edgedata + [((int(datagrp[ii][0]),int(datagrp[ii][1])))]
    return edgedata

def test_bipartite(edgedata):
    Gx = nx.DiGraph()
    Gx.add_edges_from(edgedata)
    testpartite = nx.bipartite.is_bipartite(Gx)
    if testpartite == True:
        return 1
    elif testpartite == False:
        return -1
    Gx.remove_edges_from(edgedata)

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_bip.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input15.txt'
filename = pathfile + fileinput

dataALL = inputfile(filename)
print(dataALL)

grpall = dataALL[0][0]
print('No of dataset = ' + grpall)

datazero = []
for i in range(len(dataALL)):
    if len(dataALL[i]) == 0:
        datazero.append(i)
    if i == len(dataALL) - 1:
        datazero.append(len(dataALL))
print(datazero)

print()
for j in datazero[:-1]:
    start = j
    end = datazero[datazero.index(j) + 1]
    edgedataX = dataset(dataALL, start, end)
    testbipartite = test_bipartite(edgedataX)
    print(testbipartite, end=' ')
