N, k = int(input()), 1

while N * 3 < k:
    k += 1
print(k - 1 if k * 3 > N else k)