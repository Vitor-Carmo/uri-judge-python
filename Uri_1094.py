tests = int(input())

C = 0 
R = 0
S = 0
total = 0

for i in range(tests):
    data = input().split()
    
    num_animals = int(data[0])
    type_animal = data[1]

    if type_animal == 'C':
        C += num_animals
        total += num_animals

    if type_animal == 'R':
        R += num_animals
        total += num_animals

    if type_animal == 'S':
        S += num_animals
        total += num_animals


def porcentage(x):
    return x * 100 / (C + R + S)

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(C))
print('Total de ratos: {}'.format(R))
print('Total de sapos: {}'.format(S))
print('Percentual de coelhos: {:.2f} %'.format(porcentage(C)))
print('Percentual de ratos: {:.2f} %'.format(porcentage(R)))
print('Percentual de sapos: {:.2f} %'.format(porcentage(S)))