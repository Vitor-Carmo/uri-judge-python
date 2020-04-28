from math import sqrt
n = int(input())

for j in range(n):
    x = int(input())

    i = 2
    prime = 0

    while i <= sqrt(x):
        if x % i == 0:
            prime += 1
        i += 1

    if prime == 0:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
