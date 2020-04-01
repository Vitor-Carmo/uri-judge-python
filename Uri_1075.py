number = int(input())

for num in range(1, 10001):
    if num % number == 2:
        print(num)