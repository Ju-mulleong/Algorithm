import sys
sys.stdin = open('input.txt', 'r')


def get_subset_sum(n, k, current_sum, has_element):
    global ans
    # 가지치기
    # print(f'k: {k}, current_sum: {current_sum}, ans: {ans}')

    if ans == 1:
        return

    if current_sum == 0 and has_element == True:  # 첫 시행(공집합) 아니고, 부분집합 합이 0이면 return 1해서 더이상 탐색하지 않도록 한다.
        ans = 1
        # print(f'부분집합 합이 0이 됨 k: {k}, current_sum: {current_sum}')  # 디버깅 확인용
        # 이거 이렇게 하니까 다 돌고 다시 공집합 직전으로 돌아올 때 current_sum이 0이 되는듯
        # k로 하면 안되겠다.
        return

    # elif current_sum > 0:   # 현재 부분집합 원소 합이 0보다 크면 어차피 조건 만족못하니까 돌아간다.
    #     return
    # 이 위의 구문은 원소에 음수 포함된 tc도 있어서 못쓴다.

    # 기본 파트
    if n == k:  # 부분집합이 결정되면 실행할 구문, 이 문제에서는 원소들의 합이 0이 되는지 아닌지만 알면 됨.
        # if current_sum == 0:
        #     print(current_sum)

        return

    # if-else문 아래의 생략된 return None으로 자동으로 돌아감. 근데 return있는게 직관적인것같으니까 return적자

    # 유도 파트
    else:
        bit[k] = 1
        get_subset_sum(n, k+1, current_sum + arr[k], True)


        bit[k] = 0
        get_subset_sum(n, k+1, current_sum, has_element)    # 이 함수 처음에 받은 has_element를 그대로 유지



'''
부분집합의 합이 0이 되는것이 존재하는지를 계산
단순하게, 모든 부분집합을 찾는다.
    그리고 부분집합마다 합을 구한다
    만약, 부분집합의 합이 0이 나오면 가지치기로 return한다.
    이미 부분집합의 합이 0보다 크면 가지치기로 빠져나간다.
    일단 이거 두 개?
'''


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # 배열의 길이 N
    arr = list(map(int, input().split()))
    # print(arr)

    bit = [0]*N
    ans = 0
    get_subset_sum(N, 0, 0, False)      # 초기 공집합이므로 has_element == False

    print(f'#{test_case} {ans}')