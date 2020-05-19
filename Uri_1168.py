led = [
    2, 5 , 5, 4, 5, 6, 3, 7,6,6        
]

x = int(input())
s = 0
for i in range(x):
    k = input()
    
    for j in k:
        u = int(j)
        
        s += led[u - 1]
    print('{} leds'.format(s))
    s = 0