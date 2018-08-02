__author__ = 'cromox'

import time

def inputfile(filename):
    with open(filename) as f:
        xx = [x.split() for x in f.readlines()]
        f.close()
    return xx

def timetaken_hhmmss(timestop, timestart):
    m, s = divmod(timestop - timestart, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" %(h, m, s)

def three_sum(xs):
    original_xs = xs[:]
    xs.sort()
    n = len(xs)
    for i in range(n-2):
        a = xs[i]
        j = i+1
        k = n-1
        while j < k:
            b = xs[j]
            c = xs[k]
            if a+b+c == 0:
                return sorted([original_xs.index(a)+1,
                               original_xs.index(b)+1,
                               original_xs.index(c)+1])
            elif a+b+c > 0:
                k = k-1
            else:
                j = j+1
    return [-1]

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_3sum.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input14.txt'
filename = pathfile + fileinput

listALL = inputfile(filename)

nolist = listALL[0][0]
nochar = listALL[0][1]
# print('listALL = ' + str(listALL))
print('No_lists = ' + str(nolist))
print('No_elmnts = ' + str(nochar))

time1 = time.strftime('%H:%M:%S (%d-%m-%Y)')
start1 = time.time()

for i in range(1,int(nolist)+1):
    listxx = [int(q) for q in listALL[i]]
    # print('listXX  = ' + str(listxx))
    listsumzero = three_sum(listxx)
    for i in range(len(listsumzero)):
        print(listsumzero[i], end=' ')
    print()

time2 = time.strftime('%H:%M:%S (%d-%m-%Y)')
end2 = time.time()

print('started = ' + str(time1) + ' finished = ' + str(time2))
howlong = timetaken_hhmmss(end2, start1)
print('timetaken = ' + str(howlong))