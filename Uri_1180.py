x = int(input())
y = input().split()
z = [ int(i) for i in y ]
print('Menor valor: {}'.format(min(z)))
print('Posicao: {}'.format(z.index(min(z))))