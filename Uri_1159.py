while True:
    x = int(input())

    if x == 0:
        break

    sum = 0
    for i in range(x, x + 10):
        if i % 2 == 0:
            sum += i

    print(sum)