soma = quantidade = 0 
for i in range(6):
    n = float(input())
    if n > 0:
        soma += n
        quantidade += 1
media = soma/quantidade
print('{} valores positivos'.format(quantidade))
print('{:.1f}'.format(media))
