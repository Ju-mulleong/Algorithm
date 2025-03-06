def perm(n, k):

    if k == n:
        print(A)
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]     # 바꾸기
            perm(n, k+1)
            A[k], A[i] = A[i], A[k]     # 원복


A = [1, 2, 3]
N = len(A)
perm(N, 0)