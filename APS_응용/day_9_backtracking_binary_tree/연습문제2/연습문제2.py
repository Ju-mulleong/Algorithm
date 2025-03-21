'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
'''


def dfs(n, subset, sum_v):
    # 문제조건: 원소의 합이 10이라면 출력
    if sum_v == 10:
        print(subset)
        return

    # 가지치기
    # 만약 이미 부분집합의 합이 10을 넘어간다면, return
    # 가지치기 위치 생각!!!!!!!! 모든 케이스 보지말기
    if sum_v > 10:
        return

    # 만약 n이 모집합의 길이와 같아진다면(인덱스로는 넘어간다면) return
    if n == len(main_set):
        return

    # 현재 원소를 가지고 가는 경우
    dfs(n+1, subset + [main_set[n]], sum_v + main_set[n] )
    # 현재 원소를 가지고 가지 않는 경우
    dfs(n+1, subset, sum_v)


main_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dfs(0, [], 0)