'''
원소들의 총 합이 30 이하인 부분집합의 개수 구하고, 그 부분집합들의 종류와 합 모두 출력
'''



def sum_of_set(n, k, sum_v):
    global cnt
    # 가지치기
    if sum_v > 30:
        return


    # 기본 파트
    if n == k:
        cnt += 1
        subset = []
        for i in range(k):
            subset.append(arr[i]*bit[i])
        print(f'부분집합: {subset} 원소들의 합: {sum_v}')
        return


    # 유도 파트
    else:
        bit[k] = 1
        sum_of_set(n, k+1, sum_v + arr[k])

        bit[k] = 0
        sum_of_set(n, k+1, sum_v)



cnt = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*len(arr)
sum_of_set(10, 0, 0)
print(f'합이 30이하인 부분집합들의 총 개수: {cnt}')