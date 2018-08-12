__author__ = 'cromox'

"""
( http://rosalind.info/problems/fib/ )

Problem

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the
case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous
month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of
rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after the n-th
month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2
(with F1=F2=1 to initiate the sequence). 

Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""
def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','').split(' ')
        f.close()
    return xx

def fibo_rabbit(n,k):
    if n > 1:
        return fibo_rabbit(n-1, k) + k * fibo_rabbit(n-2, k)
    elif n == 1:
        return 1
    elif n == 0:
        return 0

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_fib.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs4.txt'
filename = pathfile + fileinput

n_k = inputfile(filename)
print(n_k)

n = int(n_k[0])
k = int(n_k[1])

print(n)
print(k)
print()
print(fibo_rabbit(n,k))
