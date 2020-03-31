from math import ceil


test = int(input())

for i in range(0, test):
    position_ant = int(input())
    optimized_time = ceil(position_ant/2)
    print(optimized_time)
