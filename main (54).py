from math import sqrt
a, p = 1, int(input())
while sqrt(a) <= p:
     if sqrt(a) < p:
        print(f"{sqrt(a)} ({a})")
    a += 1