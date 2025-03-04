# import sys
# sys.stdin = open('input1.txt.txt', 'r')


# 백트래킹 함수 작성
def find_most_preferred_hamburger(n, k, point_sum, kcal_sum, banned_set):
    global max_sum
    # print(f'k: {k} point_sum: {point_sum} kcal_sum: {kcal_sum} banned_set: {banned_set}')

    # 가지치기

    # 만약 지금 point_sum에 남은 가능한 점수를 모두 합해도 최댓값을 업데이트 못 할때, return
    temp_sum = point_sum
    for j in point_list:
        if j not in banned_set:
            temp_sum += j
    if temp_sum <= max_sum:
        return

    # 매 조합마다 최대점수 업데이트
    if point_sum > max_sum:
        max_sum = point_sum

    # 기본 파트
    if n == k:  # 만약 재료를 모두 썻다면, return
        return

    # 유도 파트
    else:
        for idx in range(len(point_list)):
            if point_list[idx] not in banned_set:
                if kcal_sum + kcal_list[idx] <= L:
                    banned_set.add(point_list[idx])     # set에 추가
                    find_most_preferred_hamburger(n, k+1, point_sum + point_list[idx], kcal_sum + kcal_list[idx], banned_set)
                    banned_set.remove(point_list[idx])  # set에서 제거


T = int(input())

for test_case in range(1, 1+T):
    N, L = map(int, input().split())
    # N은 재료의 수, L은 제한 칼로리

    # 딕셔너리로 하자.
    # dict_menu = {}
    # for i in range(N):
    #     K, V = map(int, input1.txt().split())
    #     dict_menu[K] = V
    # print(dict_menu)

    point_list = [0] * N
    kcal_list = [0] * N
    # 이거 딕셔너리로 해서 느린건가? 리스트로 해볼까
    for i in range(N):
        point_list[i], kcal_list[i] = map(int, input().split())
    # print(point_list)
    # print(kcal_list)

    # 점수 기준으로 list들 묶어서 내림차순으로 설정하기
    items = sorted(zip(point_list, kcal_list), reverse=True, key=lambda x: x[0])
    # key~는 점수를 기준으로 고려한다는 뜻, reverse = True는 내림차순
    point_list, kcal_list = zip(*items)
    # zip 2번하면 원래대로..

    max_sum = 0
    find_most_preferred_hamburger(N, 0, 0, 0, set())
    print(f'#{test_case} {max_sum}')



