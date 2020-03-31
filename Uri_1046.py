hours = input().split()


inicial = int(hours[0])
final = int(hours[1])

if inicial > final:
    a = 24 - inicial
    hour = a + final

elif final > inicial:
    hour = final - inicial

else:
    hour = 24

print("O JOGO DUROU {} HORA(S)".format(hour))
    
