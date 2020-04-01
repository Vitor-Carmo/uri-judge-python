tests_cases = 100
highest_value = 0

for pos in range(tests_cases):
    num = int(input())
    
    if pos == 0:
        highest_value = num
    
    else:
        if num > highest_value:
            highest_value = num
            position = pos + 1 

print(highest_value)
print(position)
