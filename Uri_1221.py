from math import sqrt
p = int(input())

import decimal

for jfg in range(p):
    num = float(input())

    rest = 0

    if(num == 0):
        print("Not Prime")
        continue
            
    if(num == 1):
        print("Not Prime")
        continue
            
            
    if(num == 2):
        print("Prime")
        continue

    i = 2
    while (i < sqrt(num) + 1):  
        if num % i == 0:
            rest += 1
        
        if rest == 2:
            break
        i += 1

    if rest >= 1:
        print('Not Prime')
    else:
        print('Prime')