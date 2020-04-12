x = int(input())
y = int(input())


if x > y:
    aux = x
    x = y
    y = aux


Σ = 0
for i in range(x, y + 1):
    if not i % 13 == 0:
        Σ += i

print(Σ)