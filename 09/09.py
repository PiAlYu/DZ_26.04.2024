fin = open('09.csv')
l = fin.readlines()
fin.close()
l = [list(map(int, i.split(';'))) for i in l]
k = 0
for i in l:
    a, b, c = i
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    try:
        if int(s) == s and s > 0:
            k += 1
    except TypeError:
        continue
print(k)
