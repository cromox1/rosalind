__author__ = 'cromox'

"""
( http://rosalind.info/problems/dna/ )
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_dna.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs1.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
print(seqs)

char1 = []
for ii in seqs:
    if ii not in char1:
        char1.append(ii)

#print(char1)
#print(char1.sort())     ## Not sure why char1.sort() NOT WORKING
print(sorted(char1))

for ch1 in sorted(char1):
    print(seqs.count(ch1), end=' ')