while True :
	x = int(input())
	if x == 0:
		break
	print(1, end='')
	for i in range(2, x+1):
		print(' {}'.format(i), end='')
	print()


