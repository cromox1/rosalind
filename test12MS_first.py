__author__ = 'cromox'

## http://rosalind.info/problems/ms/
#
# My first attempt
# So slow... take about 11 MINUTES to finish sorting the datasets... Rosalind required less than 5 mins
#

import time

maksimum = 1 * 10**5

def inputfile(filename):
    with open(filename) as f:
        m, mlists = [line.strip().split() for line in f.readlines()]
        f.close()
        mlist = [int(num) for num in mlists]  ### list comprehension
        m = [int(num) for num in m][0] # list(map(int, m))
        return m, mlist

def insertionsort(mlist):
    istart = 1
    istop = len(mlist) - 1
    # swaps = 0

    for i in range(istart, istop + 1):
        for k in range(istop, i - 1, -1):
            totukar = mlist[k]
            ditukar = mlist[k - 1]
            if totukar < ditukar :
                mlist[k], mlist[k - 1] = ditukar, totukar  ## fastest way to SWAP
                # swaps = swaps + 1
                # print('swaps = ' + str(swaps) + ' / k = %s ' %k + ' / totukar = ' + str(totukar) + ' / ditukar = ' + str(ditukar))
    return mlist #, swaps

def merge(list1, list2):
    mallsorted = []
    i, j = 0, 0
    while (len(mallsorted) < len(list1) + len(list2)):
        if list1[i] < list2[j]:
	        mallsorted.append(list1[i])
	        i+= 1
        else:
	        mallsorted.append(list2[j])
	        j+= 1
        if i == len(list1) or j == len(list2):
	        mallsorted.extend(list1[i:] or list2[j:])
	        break
    return mallsorted

def masa_hhmmss(end, start):
    m, s = divmod(end - start, 60)
    h, m = divmod(m, 60)
    time_str = "%02d:%02d:%02d" % (h, m, s)
    return time_str

if __name__ == "__main__":

    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test8_merge_sort_aftersplit_OK_NEED_INVESTIGATE'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_ms4.txt'
    filename = filedirectory + fileinput

    inputnyer = inputfile(filename)

    m = inputnyer[0]
    mlist = inputnyer[1]

    try:
        int(m)

        if m <= maksimum and m == len(mlist):

            time1 = time.strftime('%H:%M:%S (%d-%m-%Y)')
            start1 = time.time()

            print('m = ' + str(m))
            print('mlist = ' + str(mlist))

            half = int(m/2)

            m1list = [int(num) for num in mlist[:half]]
            m2list = [int(num) for num in mlist[half:]]

            print('m1list = ' + str(m1list))
            print('m2list = ' + str(m2list))

            list1, list2 = insertionsort(m1list), insertionsort(m2list)

            mallsorted = merge(list1, list2)

            print('mallsorted = ' + str(mallsorted))

            print('')
            for val in mallsorted:
                print(val, sep=' ', end=' ')
            print('\n')
            time2 = time.strftime('%H:%M:%S (%d-%m-%Y)')
            end2 = time.time()
            print('started = ' + str(time1) + ' finished = ' + str(time2))
            timetaken = masa_hhmmss(end2, start1)
            print('timetaken = ' + str(timetaken))
            print('')

        else:
            if m > maksimum:
                terlebih = m
            print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
    except:
        print('problem with input file %s' %fileinput)
