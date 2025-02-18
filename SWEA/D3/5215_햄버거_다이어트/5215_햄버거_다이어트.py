import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, 1+T):
    N, L = map(int, input().split())
    # N은 재료의 수, L은 제한 칼로리

    # 딕셔너리로 하자.
    dict_origin_menu = {}
    for i in range(N):
        K, V = map(int, input().split())
        dict_origin_menu[K] = V
    # print(dict_menu)

    '''
    주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수
    
    !!!맛에 대한 점수의 합이 높은 것 우선, 같은 재료 여러번 사용 불가, 재료 조합에 제한 없음
    
    이거 칼로리/(재료의 맛) 해서 순서대로 일단 정리
    칼로리 대비 맛이 높은 재료가 우선적으로 많이 들어가야하지않나
    
    그런데 소수 계산하면 안될듯
    
    for로 일단 점수 높은것부터 차례대로 L에서 빼고, 
        더 이상 이 재료를 뺄 수 없으면, 그 다음 점수 높은 재료 탐색
        다시 그 재료를 한개부터..더이상 뺄 수 없을때까지 L에서 빼기.
        남은 L이 재료의 제일 적은 칼로리보다 적을 경우. lst_combination에 append하고 다음 for
    while이 나을듯?
    
    아니다 DFS인가
    같은 재료 중첩 안됨
    test_case 1 기준으로
    1. 500(1000) 하면 1000kcal로 끝. max_score에 기록
        L보다 넘치지 않고 더 넣을수있는 재료가 없으면 기록
    다시 돌아가서 400부터 시작, 딕셔너리에서 500(1000) 없애기 점수 높은 순서대로 넣어보기 점수(칼로리)
    400(400), 300(500), 250(300)    => 여기서 kcal가 1000 넘어감.
    넘어가니까 뒤로 돌아가서 그 다음 큰 점수 넣어보기
    400(400), 300(500), 100(200)    => 이것도 오버
    다시 뒤로 돌아가서 그 다음 큰 점수
    없다, 인접한 점수 다 씀  => 400(400), 300(500) 기록
    뒤로 한 번 더 돌아가서 그 다음 큰 점수 넣기
    400(400), 250(300)
    그 다음 큰 점수 넣기
    400(400), 250(300), 100(200)
    그 다음 큰 점수 넣기 => 없다. 기록 => 
    ...
    인접리스트를 어떻게 해야하나
    
    
    
    '''
    #

    print(f'#{test_case} {max_score}')

    #  or L - sum_score < min(dict_menu.keys())

    dict_menu = dict_origin_menu
    #
    # sum_kcal = 0
    # max_score = 0
    # sum_score = 0
    # while True:    # 합 칼로리가 L 안넘을때까지 반복
    #
    #     # 딕셔너리 키 중 가장 높은값부터 넣어보기
    #
    #     put_menu = max(dict_menu.keys())
    #     print(put_menu)
    #     # while L - sum_kcal >= dict_menu[put_menu]:   # L - sum_kcal이 이번에 선택한 재료칼로리보다 작아질 때 까지 반복
    #     sum_kcal += dict_menu[put_menu]     # sum_kcal에 재료 칼로리 계속 더하기
    #     print(f'sum_kcal = {sum_kcal}')
    #     sum_score += put_menu
    #     print(f'sum_score = {sum_score}')
    #     # 시행 끝나면 그 put_menu 키-값쌍 pop()으로 없애자.
    #     dict_menu.pop(put_menu)
    #
    #     if sum_score > max_score:
    #         max_score = sum_score
    #
    #     sum_score = 0       # sum_score 초기화
    #     sum_kcal = 0        # sum_kcal 초기화
    #     if dict_menu == {}:
    #         break