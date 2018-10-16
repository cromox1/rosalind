__author__ = 'cromox'

'''
Problem
In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted
alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the
corresponding amino acid.

Given: A protein string P of length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.

Sample Dataset:
SKADYEK

Sample Output:
821.392
'''
## http://rosalind.info/glossary/monoisotopic-mass-table/

masstabletxt = 'A   71.03711 \
C   103.00919 \
D   115.02694 \
E   129.04259 \
F   147.06841 \
G   57.02146 \
H   137.05891 \
I   113.08406 \
K   128.09496 \
L   113.08406 \
M   131.04049 \
N   114.04293 \
P   97.05276 \
Q   128.05858 \
R   156.10111 \
S   87.03203 \
T   101.04768 \
V   99.06841 \
W   186.07931 \
Y   163.06333 '

masstable = masstabletxt.replace(' ','#').replace('###','#').replace('##','#').replace('##','#').split('#')
# print(masstable)

massdict = {}
for i in range(int(len(masstable)/2)):
    key = masstable[i*2]
    value = masstable[i*2 + 1]
    massdict[key] = value
# print(massdict)

def inputfile(filename):
    with open(filename) as f:
        # xx = f.readlines()
        # xx = [x.split() for x in f.readlines()]
        # xx = f.read() #.split('\n')
        xx = f.read().replace('\n','')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_prtm.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs18.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
print(seqs)
# print(len(seqs))

totalmass = 0
for i in range(len(seqs)):
    seqmass = float(massdict[seqs[i]])
    print(seqs[i] + ' - > ' + str(seqmass))
    totalmass = totalmass + seqmass
print()
print(totalmass)