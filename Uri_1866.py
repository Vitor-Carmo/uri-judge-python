x = int(input())

for i in range(x):
    n = int(input())

    if not n % 2 == 0:
        x = 1
    else:
        x = 0

    print(x) 