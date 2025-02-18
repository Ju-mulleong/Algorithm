def powerset(n, k):     # k: 깊이(depth)
    # 기본파트
    if k == n:
        print(bit)
    # 유도파트
    else:
        bit[k] = 1          # 1했다가
        powerset(n, k+1)    # 한 자리 더 갔다가 돌아오면
        bit[k] = 0          # 0 해봄
        powerset(n, k+1)    # 한 자리 더 갔다가 돌아오면

        # return None


arr = [1, 2, 3]
N = len(arr)    # 3
bit = [0] * N
powerset(N, 0)      # (3, 0)