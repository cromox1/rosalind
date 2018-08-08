__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

#pathfile = r'C:\Users\cromox\Downloads\\'
#fileinput = 'rosalind_hea.txt'
pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
fileinput = 'input11.txt'
filename = pathfile + fileinput

dataALL = inputfile(filename)

nn = dataALL[0][0]
dataA = [int(x) for x in dataALL[1:][0]]

for i in range(1, int(nn)):
    while dataA[i] > dataA[int((i - 1)/2)]:
        dataA[i], dataA[int((i - 1)/2)] = dataA[int((i - 1)/2)], dataA[i]
        i = int((i - 1)/2)
print(*dataA)

