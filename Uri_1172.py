for i in range(10):
    x = int(input())
    if x < 0 or 0 == x:
        x = 1
    print('X[{}] = {}'.format(i, x))