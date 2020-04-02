hi, mi, hf, mf = map(int, input().split())

HORAS = hf - hi + 24 * int(hf < hi or (mf < mi and hf <= hi) or (hf == hi and mf == mi)) - int(mf < mi)
MINUTOS = mf - mi + 60 * int(mf < mi)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(HORAS,MINUTOS))