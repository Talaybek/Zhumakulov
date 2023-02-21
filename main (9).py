a = int(input("Введите четырехзначное число: "))
if a>999 or a<10000:
    z1 = a // 1000
    a = a % 1000
    z2 = a // 100
    a = a % 100
    z3 = a // 10
    a = a % 10
    z4 = a // 1
    s = z1 + z2 + z3 + z4
    d = z1 * z2 * z3 * z4
    print (s)
    print (d)