x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
S = 1 / 2 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
P = (((((x2 - x1) ** 2)) + ((y2 - y1) ** 2)) ** 0.5) + (((((x3 - x2) ** 2)) + ((y3 - y2) ** 2)) ** 0.5) + (((((x1 - x3) ** 2)) + ((y1 - y3) ** 2)) ** 0.5)