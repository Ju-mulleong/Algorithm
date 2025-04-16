import sys
sys.stdin = open('input.txt', 'r')


'''
묶음의 수는 주어진다.(P)
부분집합을 만들고, 길이가 P인 부분집합들만 걸러내서 최댓값 구하기
    구체적으로 예를 들어 N = 10 P = 3이면
    8, 1, 1 을 미리 줬다고 생각하고,
    8에서 1씩 빼서 하나씩 주자.
    dfs 가능은 할거같은데 좀 느릴 것 같다
    그래도 일단 dfs로 하자
    
'''

T = int(input())

for test_case in range(1, 1+T):
    # 달란트 수, 묶음의 수
    N, P = map(int, input().split())

    # 한 묶음마다 최소 1씩 주었다 생각하고 새로운 달란트 수 NN 할당
    NN = N-P+1

    dalant_lst = [1]*P
    dalant_lst[0] = NN
    # print(dalant_lst)

    max_v = 0
    while dalant_lst[0] > dalant_lst[1]:
        for i in range(1, P):
            dalant_lst[0] -= 1
            dalant_lst[i] += 1
            result = 1
            for j in range(P):
                result = result*dalant_lst[j]
                if result > max_v:
                    max_v = result

    print(f'#{test_case} {max_v}')
