__author__ = 'cromox'

def input_file_majority(filename):
    with open(filename) as f:
        mlist = [line.strip().split() for line in f.readlines()]
        f.close()
        majority = []
        nline = len(mlist)
        for i in range(1,nline):
            addornot = 0
            matrix = [int(num) for num in mlist[i]]
            halfel = int(len(matrix)/2)
            # print('matrix = ' + str(matrix) + ' // halfelement = ' + str(halfel))
            for j in list(set(matrix)):
                if matrix.count(j) > halfel:
                    # print('count of %s' %j + ' = ' + str(matrix.count(j)))
                    majority.append(j)
                    addornot = 1
            if addornot == 0:
                majority.append(-1)
        # print(str(majority))

        return mlist, nline, majority

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test6_majorityelement'
    fileinput = r'\test_input1.txt'
    # fileinput = r'\rosalind_maj.txt'
    filename = filedirectory + fileinput

    inputmajority = input_file_majority(filename)

    mlist = inputmajority[0]
    numline = inputmajority[1]
    majlist = inputmajority[2]

    # print('mlist = ' + str(mlist))
    print('numline = ' + str(numline))
    print('majlist = ' + str(majlist))

    print('')
    for val in majlist:
        print(val, sep=' ', end=' ')
    print('')
