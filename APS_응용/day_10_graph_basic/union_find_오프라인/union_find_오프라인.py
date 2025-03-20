def make_set(x):
    p[x] = x


def find_set(x):
    if x == p[x]: return x
    else: return find_set(p[x])


def find_set2(x):
    while p[x] != x:
        x = p[x]

    return x

def union(x, y):
    # 대빵끼리 인수합병
    p[find_set(y)] = p[find_set(x)]

N = 6
p = [0]*(N+1)
for i in range(1, 1+N):
    make_set(i)

# p = [i for i in range(1, N+1)]
# p = list(range(1, 1+N))
print(p)
union(1, 3)
print(p)
union(2, 3)
print(p)
