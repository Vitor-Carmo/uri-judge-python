real_logic = '''
            actually the real logic is this:
            +-----------------------------------------------------+
                import decimal

                def drange(x, y, jump):
                    while x <= y:
                        yield float(x)
                        x += float(decimal.Decimal(jump))
                z = 1
                y = 3

                for i in drange(0, 2, 0.2):
                    for j in drange(z, y, 1):
                        print('I={:.1f} J={:.1f}'.format(i, j))

                    z += 0.2
                    y += 0.2    
            +------------------------------------------------------+

            but the problem have some sh*t with decimals
            so i had to do what i've do

            (sorry about my english,)
            '''

import decimal


#   I saw this function on the stack overflow, this basically
#   can use decimals in interactions to jump

def drange(x, y, jump):
    while x <= y:
        yield float(x)
        x += float(decimal.Decimal(jump))
            

z = 1
y = 3
for i in drange(0, 2, 0.2):
    for j in drange(z, y, 1):
        if i == int(i):
            i = int(i)
            print('I={}'.format(i), end=' ')
        else:
            if i == 1.9999999999999998:
                i = 2
                print('I={}'.format(i), end=' ')
            else:
                print('I={:.1f}'.format(i), end=' ')


        if j == int(j):
            j = int(j)
            print('J={}'.format(j), end='\n')
            
        else:
            if j == 1.9999999999999998:
                j = 2
                print('J={}'.format(j), end='\n')

            elif j == 3.0000000000000004:
                j = 3
                print('J={}'.format(j), end='\n') 

            else:
                print('J={:.1f}'.format(j), end='\n') 
        
    z += 0.2
    y += 0.2


