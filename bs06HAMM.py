__author__ = 'cromox'

'''
( http://rosalind.info/problems/hamm/ )

Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''
def inputfile(filename):
    with open(filename) as f:
        # xx = f.readlines()
        # xx = [x.split() for x in f.readlines()]
        xx = f.read().split('\n')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_hamm.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs6.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
print(seqs)

ss = seqs[0]
tt = seqs[1]

print('ss = ' + ss + '\n' + 'tt = ' + tt)

mismatch = 0

for i in range(len(ss)):
    if ss[i] != tt[i]:
        mismatch = mismatch + 1

print()
print(mismatch)
