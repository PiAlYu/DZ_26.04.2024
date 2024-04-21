from itertools import product

a = [str(i) + str(j) for i in '02468ac' for j in '02468ac']
b = [str(i) + str(j) for i in '13579b' for j in '13579b']
k = 0
for i in product('0123456789abc', repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        if s.count('2') == 1:
            if all(i not in s for i in a):
                if all(i not in s for i in b):
                    k += 1
print(k)
