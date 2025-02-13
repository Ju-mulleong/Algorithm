def f(i, N):
    if i == N:      # 중단조건
        return
    else:           # 재귀호출
        print(i)
        f(i+1, N)

f(0, 3)
# f(0, 1000)      # RecursionError: maximum recursion depth exceeded while calling a Python object
