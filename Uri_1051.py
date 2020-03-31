money = float(input())


if 0 < money <= 2000:
    print("Isento")


elif 2000 < money <= 3000:
    t = money - 2000
    t1 = t * 0.08
    print("R$ %.2f"%t1) #new way to print a number


elif 3000 < money <= 4500:
    t = money - 2000
    t1 = t - 1000
    tx1 = 1000 * 0.08
    tx2 = t1 * 0.18
    print("R$ %.2f"%(tx1+tx2))

else:
    t = money - 2000
    t1 = t - 1000
    tx1 = 1000 * 0.08
    t2 = t1 - 1500
    tx2 = 1500 * 0.18
    tx = t2 * 0.28
    print("R$ %.2f" %(tx+tx1+tx2))
