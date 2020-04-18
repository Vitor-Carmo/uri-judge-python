i = 0
idade = 1
idades = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        idades += idade
        i += 1


media = idades / i
print('{:.2f}'.format(media))