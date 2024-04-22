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
    if all(game(i) == 'p1' for i in moves(array)):
        return 'v1'
    if any(game(i) == 'v1' for i in moves(array)):
        return 'p2'

for s in range(1, 72):
    if game((8, s)) == 'p2':
        print(s)