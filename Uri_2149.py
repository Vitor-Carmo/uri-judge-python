sequence = [0, 1, 1, 1, 2, 2]

for i in range(6, 20):
    if (i-1) % 2 == 0:
        sequence.append(sequence[i-1] * sequence[i-2])
    else:
        sequence.append(sequence[i-1] + sequence[i-2])
while True:
    try:
        n = int(input())
        print(sequence[n - 1])
    except EOFError:
        break