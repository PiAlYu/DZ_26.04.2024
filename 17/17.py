fin = open('17.txt')
a = fin.readlines()
fin.close()
a = [int(i) for i in a]
s, k, m = sum(a) / len(a), 0, -float('inf')
for i in range(len(a) - 1):
    if a[i] % 10 == 9 or a[i + 1] % 10 == 9:
        if a[i] < s and a[i + 1] < s:
            k += 1
            m = max(m, a[i] + a[i + 1])
print(k, m)