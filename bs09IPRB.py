__author__ = 'cromox'

'''
Problem

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are
homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().split(' ')
        f.close()
    return xx

def mendel_first_law(k, m, n):
    total_pop = k + m + n

    # k = total of AA
    # m = total of Aa
    # n = total of aa
    # Probability to get recessive phenotype - aa
    # 1. aa x aa = 1.0
    # 2. aa x Aa = 0.5
    # 3. Aa x aa = 0.5
    # 4. Aa x Aa = 0.25
    # 5. AA x AA = 0.0

    PRone = ( n / total_pop) * ( (n - 1) / (total_pop - 1)) * 1
    PRtwo = ( n / total_pop) * ( m / (total_pop - 1)) * 0.5
    PRtri = ( m / total_pop) * ( n / (total_pop - 1)) * 0.5
    PRfor = ( m / total_pop) * ( (m - 1) / (total_pop - 1)) * 0.25

    # Probablity Dominant AA = 1 - (Probablity of recessive - aa)
    print(1 - (PRone + PRtwo + PRtri + PRfor))

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_iprb.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs9.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)

xx = [int(x) for x in seqs]
print(xx)
k = xx[0]
m = xx[1]
n = xx[2]

mendel_first_law(k, m, n)
