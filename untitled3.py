a = 123
if a>99 or a<1000:
    z1 = a // 100
    a = a % 100
    z2 = a // 10
    z2 = z2 * 10
    z3 = a % 10
    z3 = z3 *100
    b = z1 + z2 +z3
    x = a - b
    print (x)