__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_ps.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input25.txt'
filename = pathfile + fileinput

dataALL = inputfile(filename)

elmnt = int(dataALL[0][0])
data0 = [int(x) for x in dataALL[1:][0]]
kk = int(dataALL[2][0])

print('No_of_Elements = ' + str(elmnt))
print('data0 = ' + str(data0))
print('k = ' + str(kk))

def swapp(list0, a, b):
    list0[a],list0[b] = list0[b],list0[a]

def heapify(list0, end, i):
    lefti = 2 * i + 1
    rghti = 2 * (i + 1)
    max = i
    if lefti < end and list0[i] < list0[lefti]:
        max = lefti
    if rghti < end and list0[max] < list0[rghti]:
        max = rghti
    if max != i:
        swapp(list0, i, max)
        heapify(list0, end, max)

def heap_sort(list0):
    end = len(list0)
    start = int(end/2) - 1
    for i in range(start, -1, -1):
        heapify(list0, end, i)
    for i in range(end - 1, 0, -1):
        swapp(list0, i, 0)
        heapify(list0, i, 0)
    return list0

data1 = heap_sort(data0)
# print('data1 = ' + str(data1))

print()
print(*data1)
print()
