from fnmatch import fnmatch

def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = [i for i in range(2, 10000) if is_simple(i)]

def f(n):
    s = []
    i = 0
    while n > 1:
        while n % a[i] == 0 and n > 1:
            s.append(a[i])
            n = n // a[i]
        i += 1
    return s

for i in range(10 ** 4 + 1):
    if fnmatch(str(i), '*2?2'):
        s = f(i)
        if len(s) == 7:
            print(i, s[-1])
