pares = impares = negativos = positivos = 0

for c in range(5):
    i = int(input())
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
    if i > 0:
        positivos += 1
    elif i < 0:
        negativos += 1

print('''{} valor(es) par(es)
{} valor(es) impar(es)
{} valor(es) positivo(s)
{} valor(es) negativo(s)'''.format(pares, impares, positivos, negativos))
