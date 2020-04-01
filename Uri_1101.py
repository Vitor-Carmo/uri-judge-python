while True:
    x, y = map( int, input().split() )
    if x <= 0 or y <= 0:
        break 

    if x > y:
        Sum = 0
        for i in range(y, x + 1):
            print(i, end=' ')
            Sum += i
        print('Sum={}'.format(Sum))
    else:
        Sum = 0
        for i in range(x, y + 1):
            print(i, end=' ')
            Sum += i
        print('Sum={}'.format(Sum))

