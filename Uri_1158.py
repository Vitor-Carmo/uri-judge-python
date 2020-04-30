d = int(input())

for i in range(d):
    sum = 0

    x, y = list( map(int, input().split()) )

    for v in range(y):
        while x % 2 == 0:
            x += 1
        sum += x
        x += 1

    print(sum)    