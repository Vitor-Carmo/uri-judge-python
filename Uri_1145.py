x, y = list(map(int, input().split()))

c = 1

for i in range(1, int(y / x) + 1):
    
    num = ""

    for y in range(x):
        num += str(c) + " "
        c += 1

    print(num[:-1])