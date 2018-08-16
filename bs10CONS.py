__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','').split('>')
        f.close()
    return xx

def dict_fastaformat(seqsfasta):
    dctdata = {}
    for seq in seqsfasta:
        if len(seq) > 0:
            for i in range(len(seq)):
                try:
                    y = int(seq[i-1])
                    x = seq[i]
                    if type(y) == int and x in 'ACGT':
                        div1 = i
                except:
                    pass
            if div1 > 0:
                key = seq[:div1]
                value = seq[div1:]
                dctdata[key] = value
    return dctdata

def carikey(dict, value):
    for k,v in dict.items():
        if v == value:
            return k

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_cons.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs10.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
dctdata = dict_fastaformat(seqs)
print(dctdata)

firstkey = list(dctdata.keys())[0]
print('no_of_char = ' + str(len(dctdata[firstkey])))

ancestor = []
mtrxrctg = []
for i in range(len(dctdata[firstkey])):
    cA = cC = cG = cT = 0
    data = {}
    for v in dctdata.values():
        if v[i] == 'A':
            cA += 1
            data['A'] = cA
        elif v[i] == 'C':
            cC += 1
            data['C'] = cC
        elif v[i] == 'G':
            cG += 1
            data['G'] = cG
        elif v[i] == 'T':
            cT += 1
            data['T'] = cT
    datatwo = [cA, cC, cG, cT]
    mtrxrctg.append(datatwo)
    ancestor.append(carikey(data,max(datatwo)))

print()
print(*ancestor, sep='')

def printmatrix(listmatrix, char, char_location):
    print(char + ':', end=' ')
    for i in range(len(listmatrix)):
        print(listmatrix[i][char_location], end=' ')
    print()

printmatrix(mtrxrctg, 'A', 0)
printmatrix(mtrxrctg, 'C', 1)
printmatrix(mtrxrctg, 'G', 2)
printmatrix(mtrxrctg, 'T', 3)



