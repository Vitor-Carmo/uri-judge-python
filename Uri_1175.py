array = []
for i in range(20):
	n = int(input())
	array.append(n)
array.reverse()
for x,i in enumerate(array):
	print('N[{}] = {}'.format(x,i))
