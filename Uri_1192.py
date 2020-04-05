testes = int(input())


for i in range(testes):
    input_ = input()


    P1 = int(input_[0])
    letter = input_[1]
    P2 = int(input_[2])


    if P1 == P2:
        output = P1 * P2

    elif letter == letter.upper():
        output = P2 - P1

    else:
        output = P1 + P2

    print(output)
