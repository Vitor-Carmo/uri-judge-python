while True:
    
    n1 = float(input())
    while not 0 <= n1 <=10:
        print('nota invalida')
        n1 = float(input())


    n2 = float(input())
    while not 0 <= n2 <= 10:
        print('nota invalida')
        n2 = float(input())


    m = (n1 + n2) / 2
    print('media = {:.2f}'.format(m))


    response = int(input('novo calculo (1-sim 2-nao)\n'))

    while not response == 1 and not response == 2:
        response = int(input('novo calculo (1-sim 2-nao)\n'))
        if response == 1 or response == 2:
            break

    if response == 2:
        break
