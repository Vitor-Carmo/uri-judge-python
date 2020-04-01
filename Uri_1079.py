tests = int(input())

for test in range(tests):
    numbers = input().split()
    
    n1 = float(numbers[0])
    n2 = float(numbers[1])
    n3 = float(numbers[2])

    weighted_average = ( (n1 * 2) + (n2 * 3) + (n3 * 5) ) / 10

    print('{:.1f}'.format(weighted_average))