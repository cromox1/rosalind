__author__ = 'cromox'

'''
( http://rosalind.info/problems/prot/ )

Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except
for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string
will incorporate protein strings along with DNA strings and RNA strings.
The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
'''

codontabletxt = "UUU F      CUU L      AUU I      GUU V  \
UUC F      CUC L      AUC I      GUC V  \
UUA L      CUA L      AUA I      GUA V  \
UUG L      CUG L      AUG M      GUG V  \
UCU S      CCU P      ACU T      GCU A  \
UCC S      CCC P      ACC T      GCC A  \
UCA S      CCA P      ACA T      GCA A  \
UCG S      CCG P      ACG T      GCG A  \
UAU Y      CAU H      AAU N      GAU D  \
UAC Y      CAC H      AAC N      GAC D  \
UAA Stop   CAA Q      AAA K      GAA E  \
UAG Stop   CAG Q      AAG K      GAG E  \
UGU C      CGU R      AGU S      GGU G  \
UGC C      CGC R      AGC S      GGC G  \
UGA Stop   CGA R      AGA R      GGA G  \
UGG W      CGG R      AGG R      GGG G"
## copy from http://rosalind.info/glossary/rna-codon-table/

codontable = codontabletxt.replace(' ','#').replace('###','#').replace('##','#').replace('##','#').split('#')
# print(codontable)

codondict = {}
for i in range(int(len(codontable)/2)):
    key = codontable[i*2]
    value = codontable[i*2 + 1]
    codondict[key] = value
# print(codondict)

def inputfile(filename):
    with open(filename) as f:
        # xx = f.readlines()
        # xx = [x.split() for x in f.readlines()]
        xx = f.read() #.split('\n')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_prot.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs11.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
print(seqs)
# print(len(seqs))

for i in range(1, len(seqs)+1):
    if i%3 == 0:
        key3 = seqs[i-3:i]
        # print(key3, end=' ')
        print(codondict[key3].replace('Stop',''), end='')
