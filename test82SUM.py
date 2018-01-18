__author__ = 'cromox'

import time

def masa_hhmmss(end, start):
    m, s = divmod(end - start, 60)
    h, m = divmod(m, 60)
    time_str = "%02d:%02d:%02d" % (h, m, s)
    return time_str

def input_file_majority(filename):
    with open(filename) as f:
        mlist = [line.strip().split() for line in f.readlines()]
        f.close()
        twosumall = []
        nline = len(mlist)
        nmatrix = [int(num) for num in mlist[0]][0]
        nelement = [int(num) for num in mlist[0]][1]
        for i in range(1,nline):
            minusone = 1
            twosum = []
            matrix = [int(num) for num in mlist[i]]
            # print('matrix = ' + str(matrix))
            for j in range(nelement):
                for k in range(j+1,nelement):
                    if matrix[j] == -matrix[k]:
                        twosum.append(j+1)
                        twosum.append(k+1)
                        minusone = 0
                        break
            # print('twosum = ' + str(twosum))
            if minusone == 0:
                twosumall.append([twosum[-2],twosum[-1]])
                # twosumall.append(twosum[1])
            elif minusone == 1:
                twosumall.append([-1])
        # print('2SUM = ' + str(twosumall))
        return mlist, nline, nmatrix, nelement, twosumall

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test9_2sum_positif_negetif'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_2sum.txt'
    filename = filedirectory + fileinput

    time1 = time.strftime('%H:%M:%S (%d-%m-%Y)')
    start1 = time.time()

    inputnyer = input_file_majority(filename)

    print('mlist = ' + str(inputnyer[0]))
    print('line = ' + str(inputnyer[1]))
    print('nmatrix = ' + str(inputnyer[2]))
    print('nelement = ' + str(inputnyer[3]))
    print('2SUM = ' + str(inputnyer[4]))
    print('')

    time2 = time.strftime('%H:%M:%S (%d-%m-%Y)')
    end2 = time.time()
    print('started = ' + str(time1) + ' finished = ' + str(time2))
    timetaken = masa_hhmmss(end2, start1)
    print('timetaken = ' + str(timetaken))

    print('')
    for val in inputnyer[4]:
        size2sum = len(val)
        if size2sum == 1:
            print(val[0], sep=' ', end=' ')
        elif size2sum > 1:
            for i in range(size2sum):
                print(val[i], sep=' ', end=' ')
        print('')
    print('')
