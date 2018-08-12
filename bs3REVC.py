__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','')
        f.close()
    return xx

def changecharviceversa(dnastring, char1, char2):
    str1 = dnastring.replace(char1,'#')
    str2 = str1.replace(char2,char1)
    str3 = str2.replace('#',char2)
    return str3

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_revc.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs3.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
print(seqs)

seqsc = seqs[::-1]
print(seqsc)

text1 = changecharviceversa(seqsc, 'A', 'T')
text2 = changecharviceversa(text1, 'C', 'G')
print()
print(text2)


