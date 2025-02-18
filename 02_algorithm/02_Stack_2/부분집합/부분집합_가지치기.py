def powerset(n, k, cursum):     # k: 깊이(depth)  cursum: current_sum, 현재 원소들의 합
    # 가지치기
    if cursum > 10: return  # 현재 원소들의 합이 10이 넘어가면 어차피 조건 만족 못하는거니까 돌아간다.

    # 기본파트
    if k == n:
        if cursum == 10:    # 원소들의 합이 10인 부분집합 출력
            print(bit)

    # 유도파트
    else:
        bit[k] = 1          # 1했다가
        powerset(n, k+1, cursum + arr[k])    # 한 자리 더 갔다가 돌아오면

        bit[k] = 0          # 0 해봄
        powerset(n, k+1, cursum)    # 한 자리 더 갔다가 돌아오면

    # return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)    # 3
bit = [0] * N
powerset(N, 0, 0)      # (3, 0)

'''
cnt로 부분집합의 합이 10인 집합의 개수도 알 수 있다!
이게 상태우선탐색?
'''