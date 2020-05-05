x = input()
t = list(map(int, input().split()))
print( t.index( min( t ) ) + 1 )