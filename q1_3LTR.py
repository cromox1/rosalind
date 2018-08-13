__author__ = 'cromox'

"""
Question 1:
Write a function which takes as its input a string containing only the letters 'A', 'C', 'G', and 'T'.
This function should print out the number of times each unique sub-sequence of three letters appears.

For example, if the input string was "ACTACTTAC", the output would be something like:
ACT: 2
CTA: 1
TAC: 2
CTT: 1
TTA: 1

The order of the sub-sequences in the output does not matter.
"""

def count_3char(input1):
    letterscan = []
    for i in range(len(input1)-2):
        char1 = input1[i:i+3]
        if char1 in input1 and char1 not in letterscan:
            letterscan.append(input1[i:i+3])

    print(letterscan)

    count={}
    for out1 in letterscan:
        key,value = out1, input1.count(out1)
        count[key] = value

    print(count)

    for key,value in count.items():
        print(key+": "+str(value), end='\n')

ss = "ACTACTTACGATAC"

count_3char(ss)
