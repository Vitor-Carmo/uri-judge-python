repeat = int(input())

iin  = out = 0

for i in range(repeat):
    
    x = int(input())

    if 10 <= x <= 20: 
        iin += 1
    else:
        out += 1

print('{} in'.format(iin))
print('{} out'.format(out))


