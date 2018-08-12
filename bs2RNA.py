__author__ = 'cromox'

"""
( http://rosalind.info/problems/rna/ )
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_rna.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs2.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
# print(seqs)
print(seqs.replace('T','U'))