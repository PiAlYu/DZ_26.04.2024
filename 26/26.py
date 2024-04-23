from functools import lru_cache

@lru_cache(maxsize=None)
def find_index(lst, n):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > n:
            right = mid - 1
        else:
            left = mid + 1

    return left if left < 10 ** 5 else left + 1

f = open('26.txt').readlines()
n, groups, classrooms = int(f[0]), list(map(int, f[1].split())), list(map(int, f[2].split()))
groups.sort()
classrooms.sort()
groups = tuple(groups)
k = 1
flag = 0
for i in range(n):
    if flag == 0:
        f = classrooms[i]
        ind = find_index(groups, f)
        if ind == 100001:
            flag = 1
        k *= ind - i
    else:
        k *= 100001 - i

print(k%100000007, find_index(groups, classrooms[0]))