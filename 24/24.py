fin = open('24.txt')
a = fin.readline()
fin.close()
k, m = 1, 0
for i in range(len(a) - 1):
    if int(a[i]) < int(a[i + 1]):
        k += 1
    else:
        if k == 5:
            m += 1
        k = 1
print(m)