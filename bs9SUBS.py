__author__ = 'cromox'

'''
( http://rosalind.info/problems/subs/ )

Problem

Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a
result, t must be no longer than s).
The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it
occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
'''

def inputfile(filename):
    with open(filename) as f:
        # xx = f.readlines()
        # xx = [x.split() for x in f.readlines()]
        xx = f.read().split('\n')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_subs.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs9.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
print(seqs)

ss = seqs[0]
sb = seqs[1]

print('ss = ' + ss + '\n' + 'sb = ' + sb)

sbx = len(sb)
# print(sbx)

print()
for i in range(len(ss)):
    if ss[i:i+sbx] == sb:
        print(i+1, end=' ')

