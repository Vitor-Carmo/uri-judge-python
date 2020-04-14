n = int(input())

for tests in range(n):
    x, y = map(int, input().split())

    if x > y:
        aux = x
        x = y
        y = aux

    Σ = 0
    for i in range(x + 1 , y):
        if not i % 2 == 0:
            Σ += i

    print(Σ)