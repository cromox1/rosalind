__author__ = 'cromox'

nombor = int(input('Masukkan int = '))
# nombor = 20

## my solution / answer
def f(n):
    if n > 1:
        return f(n-1) + f(n-2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0

print(f(nombor))

### other solution :

##1)
#def fibonacci(n):
#    a, b = 0, 1
#    for i in xrange(0, n):
#        a, b = b, a + b
#    return a

##2)
#def fibonacci(f1=1L, f2=1L):
#    '''Fibonacci sequence generator.'''
#    yield f1; yield f2
#    while True:
#        f1, f2 = f2, f1 + f2
#        yield f2

##3)
#    n=25 #example
#    f=[1]+[0]
#    for i in range(n):
#        f=[sum(f)] + f[:-1]
#    print f[1]

##4)
def fib(n):
  if n==0:
    return 0
  f=[0, 1]
  for i in range(2, n+1):
    f.append(f[i-1]+f[i-2])
  return f[n]

print(fib(nombor))
