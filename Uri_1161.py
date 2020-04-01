def fatorial(x):
    return 1 if x < 2 else fatorial(x-1)*x 


while True:
    try:
        _in =  input().split()

        a = int(_in[0])
        b = int(_in[1])

        fat = fatorial(a) + fatorial(b)

        print(fat)
        
    except:
        
        break