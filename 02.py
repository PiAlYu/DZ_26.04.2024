print('x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (w <= z) and((y <= x) == (z <= y))
                s = f'{x}{y}{z}{w}'
                if f == 1 and s.count('0') != 4 and s.count('1') != 4:
                    print(x, y, z, w, f)
