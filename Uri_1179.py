
par = []
impar = []

for y in range(15):
    if len(par) == 5:
            for i,j in enumerate(par):
                print('par[{}] = {}'.format(i, j))
            par = []

    if len(impar) == 5:
        for i,j in enumerate(impar):
            print('impar[{}] = {}'.format(i, j))
        impar = []

    num = int(input())
    
    par_impar = num % 2 == 0

    if par_impar:
        par.append(num)
    else:
        impar.append(num)


if len(impar) > 0:
    for i,j in enumerate(impar):
        print('impar[{}] = {}'.format(i, j))


if len(par) > 0:
    for i,j in enumerate(par):
        print('par[{}] = {}'.format(i, j))
