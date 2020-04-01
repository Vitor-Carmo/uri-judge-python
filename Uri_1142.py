out = '''1 2 3 PUM
         5 6 7 PUM
         9 10 11 PUM
         13 14 15 PUM
         17 18 19 PUM
         21 22 23 PUM
         25 26 27 PUM '''

num = int(input())

for n in range(1, num * 4 + 1):
    if n % 4 ==0:
        print('PUM')
    else:
        print(n, end=' ')