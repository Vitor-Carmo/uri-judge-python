def beggin():
    text = input().split()
    i, j = map(int, input().split())

    sum = i + j

    return text, sum



def odd_even(sum):
    if sum % 2 == 0:
        return'PAR'

    return  'IMPAR'


def who_win(p , text):
    if text.index(p) == 1:
        
        return text[0]

    return text[2]



n = int(input())
for i in range(n):
    text, sum = beggin()
    p = odd_even(sum)

    print(who_win(p, text))