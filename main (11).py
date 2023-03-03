b = int(input("Введите нижнее основание: "))
a = int(input("Введите верхнее основание: "))
h = int(input("Введите высоту: "))
if a < b:
    HM = b - a
    AHMD = b - HM
    AH = AHMD // 2
    AB2 = AH *AH + h * h
    import math 
    n = AB2
    sqrt = math.sqrt(n)
    P = b + a + sqrt + sqrt
    print (P)