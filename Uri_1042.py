values = input().split()
values_copy = values[:]
for c,i in enumerate(values):
    values[c] = int(i)
list.sort(values)
for valor in values:
    print(valor)
print()
for i in values_copy:
    print(i)