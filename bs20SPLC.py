__author__ = 'cromox'

codontabletxt = 'UUU F      CUU L      AUU I      GUU V  \
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
UGG W      CGG R      AGG R      GGG G'
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
        xx = f.read().replace('\n','').split('>')
        f.close()
    return xx

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_splc.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs20.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)

dctdata = {}
for seq in seqs:
    for i in range(len(seq)):
        try:
            y = int(seq[i-1])
            x = seq[i]
            if type(y) == int and x in 'ACGT':
                div1 = i
        except:
            pass
    if len(seq) > 0:
        # print(seq)
        key = seq[:div1]
        value = seq[div1:]
        dctdata[key] = value
print(dctdata)

rnadata = []
for v in dctdata.values():
    rnadata.append(v)

xrna = rnadata[0]
print(xrna)

for i in range(1, len(rnadata)):
    xrna = xrna.replace(rnadata[i],'')
print(xrna)

rnatoconvert = xrna.replace('T','U')
print()
for i in range(1, len(rnatoconvert)+1):
    if i%3 == 0:
        key3 = rnatoconvert[i-3:i]
        print(codondict[key3].replace('Stop',''), end='')


