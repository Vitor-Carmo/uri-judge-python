z = 7
y = 4
for i in range(1, 10, 2):
    for j in range(z, y, -1):
        print('I={} J={}'.format(i, j))
    z +=2
    y += 2