x = int(input())
for j in range(x):
    n = int(input())

    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum+= i

    if sum == n:
        print('{} eh perfeito'.format(n))
    else:
        print('{} nao eh perfeito'.format(n))
