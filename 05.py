a = []
for n in range(1, 100):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + '010'
    else:
        r = r + bin((n % 3) * 5)[2:]
    r = int(r, 2)
    if r > 300 and r % 2 == 0:
        a.append([r, n])
a.sort()
print(a[0][1])