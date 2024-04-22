from functools import lru_cache

def moves(array):
    a, b = array
    return (a + 1, b), (a, b + 1), (a + b, b), (a, b + a)

@lru_cache(None)
def game(array):
    if sum(array) >= 80:
        return 'end'
    if any(game(i) == 'end' for i in moves(array)):
        return 'p1'
    if any(game(i) == 'p1' for i in moves(array)):
        return 'v1'

for s in range(1, 72):
    if game((8, s)) == 'v1':
        print(s)