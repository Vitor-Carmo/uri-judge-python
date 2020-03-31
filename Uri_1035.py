values = input().split()


a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
