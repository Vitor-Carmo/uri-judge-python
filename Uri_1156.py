s = 1
x = 3 
y = 2 
while x < 40:
  s += x / y
  x += 2
  y *= 2 
print('{:.2f}'.format(s))