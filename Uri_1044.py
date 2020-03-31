def multiple(x, y):
    for i in range (y+1):
        if x * i == y:
            return 'Sao Multiplos'

    return 'Nao sao Multiplos'


number =  input().split()

a = int(number[0])
b = int(number[1])


if   a < b: 
    print(multiple(a, b)) 
else: 
    print(multiple(b, a))

