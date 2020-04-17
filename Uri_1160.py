T = int(input())

for t in range(T):
    data = input().split()

    A = int(data[0])
    B = int(data[1])
    taxaA = float(data[2])
    taxaB = float(data[3])

    ano = 0

    while A <= B:
        A += int( A * (taxaA / 100) ) 
        B += int( B * (taxaB / 100) )
        ano += 1

        if ano > 100:
            print('Mais de 1 seculo.')
            break
            
    if not ano > 100:
        print('{} anos.'.format(ano))
