__author__ = 'cromox'
'''
( http://rosalind.info/problems/lcsm/ )

Problem

A common substring of a collection of strings is a substring of every member of the collection. We say that a common
substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a
common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest
common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest
common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''


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

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_lcsm.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs13.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
dctdata = dict_fastaformat(seqs)
# print(dctdata)

allseqs = []
for v in dctdata.values():
    allseqs.append(v)
print(allseqs)

lngmin = min(len(x) for x in allseqs)
print('lngmin = ' + str(lngmin))
seqmin = [x for x in allseqs if len(x) == lngmin][-1]
print('seqmin = ' + seqmin)
xseqmins = [x for x in allseqs if x != seqmin]
print()

def longestcommonstring(lngmin, seqmin, xseqmins):
    for j in range(lngmin, 1, -1):
        for s in range(0, lngmin - j + 1):
            if s < j + s:
                # print(str(seqmin[s:j+s]) + ' / s = ' + str(s) + ' / j+s = ' + str(j+s))
                comstring = seqmin[s:j+s]
                if all(seq.find(comstring) >= 0 for seq in xseqmins):
                    return comstring

longestcomm = longestcommonstring(lngmin, seqmin, xseqmins)

print(len(longestcomm))
print()
print(longestcomm)


