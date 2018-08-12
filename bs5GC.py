__author__ = 'cromox'
"""
( http://rosalind.info/problems/gc/ )

Problem

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example,
the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes
a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless otherwise stated
"""

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','').split('>')
        f.close()
    return xx

#pathfile = r'C:\Users\cromox\Downloads\\'
#fileinput = 'rosalind_gc.txt'
pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
fileinput = 'input_bs5.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
# print(seqs)

dctdata = {}
for seq in seqs:
    if len(seq) > 0:
        print(seq)
        key = seq[:13]
        value = seq[13:]
        dctdata[key] = value

#print('dctdata # = ' + str(dctdata))

percentage = dict({(k,(v.count('G')+v.count('C'))*100/len(v)) for k,v in dctdata.items()})
print(percentage)

print()
for k,v in percentage.items():
    if v == max(percentage.values()):
        print(k + '\n' + str(v))

