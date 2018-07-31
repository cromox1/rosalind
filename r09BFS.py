__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

#pathfile = r'C:\Users\cromox\Downloads\\'
#fileinput = 'rosalind_bfs.txt'
pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
fileinput = 'input15.txt'
filename = pathfile + fileinput

data1 = inputfile(filename)
# print(data1)
baris = data1[0][1]
compn = data1[0][0]

data0 = data1[1:]

print('Bil_network = ' + str(baris) + ' / Bil_nodes = ' + str(compn))
print(data0)

netdata = []
for ii in range(len(data0)):
    netdata = netdata + [((int(data0[ii][0]),int(data0[ii][1])))]
print(netdata)

import networkx as nx
import matplotlib.pyplot as plt

Gx = nx.DiGraph()
# Gx.add_nodes_from(range(7))
Gx.add_edges_from(netdata)
print("Nodes of graph: ")
print(Gx.nodes())
print("Edges of graph: ")
print(Gx.edges())

dists = nx.single_source_shortest_path_length(Gx, 1)
matrx = list(Gx.nodes())
matrx.sort()
print('Matrix = ' + str(matrx))
print('Bil_nodes_Matrx = ' + str(len(matrx)))

#for n in matrx:
#    print(dists.get(n, -1),end=' ')
#print()

for n in range(1, int(compn)+1):
    print(dists.get(n, -1),end=' ')
print()

nx.draw(Gx, with_labels=True)
# plt.savefig("simple_path.png") # save as png
plt.show() # display