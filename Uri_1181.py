line = int(input())
operation = input()   
sum = 0

for i in range(12):
    for j in range(12):
        value = float(input())
        if i == line:
            sum += value
               
if operation == 'S':
    print("%.1f" %sum)
else:
    print("%.1f" %(sum/12))