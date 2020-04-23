n = []
x = float(input())
n.append(x)
for i in range(1, 101):
    print('N[{}] = {:.4f}'.format(i-1, n[i - 1]))
    n.append(n[i - 1] / 2)