a = int(input("Введите пятизначное число: "))
if a>9999 or a<100000:
    a = a % 100
    z1 = a // 10
    a = a % 10
    print (a)
    print (z)