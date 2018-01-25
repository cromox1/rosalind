__author__ = 'cromox'

def merge(left, right):
	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break
	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = int(len(list)/2)
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)

def inputfile(filename):
    with open(filename) as f:
        m, mlists = [line.strip().split() for line in f.readlines()]
        f.close()
        mlist = [int(num) for num in mlists]  ### list comprehension
        m = [int(num) for num in m][0] # list(map(int, m))
        return m, mlist

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test8_merge_sort_aftersplit_OK_NEED_INVESTIGATE'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_ms4.txt'
    filename = filedirectory + fileinput

    inputnyer = inputfile(filename)

    m = inputnyer[0]
    matrix = inputnyer[1]

    matrixall = mergesort(matrix)    

    print('')
    for val in matrixall:
        print(val, sep=' ', end=' ')
    print('')
