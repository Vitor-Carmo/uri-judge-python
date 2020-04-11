C = int(input())
for y in range(C):
    crypto = input()
    decode = ''.join(s for s in crypto if s.islower())
    decode = decode[::-1]
    print(decode)