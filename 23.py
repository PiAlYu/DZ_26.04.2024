def f(a, b, h):
    if a == b: return h
    if a > b: return ''
    return f'{f(a * 2, b, h + 'a')} {f(a + 3, b, h + 'b')}'

k = 0
s = f(2, 38, '').split()
for i in s:
    if 'aba' in i:
        k += 1
print(k)