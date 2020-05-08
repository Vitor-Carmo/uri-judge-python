while True:
    try:
        x = int(input())
        lesmas = list(map(int, input().split()))
        lesmas_max = max(lesmas)

        if lesmas_max < 10:
            print(1)
        elif lesmas_max < 20:
            print(2)
        else:
            print(3)
    except:
        break