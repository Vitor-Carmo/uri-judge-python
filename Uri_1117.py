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