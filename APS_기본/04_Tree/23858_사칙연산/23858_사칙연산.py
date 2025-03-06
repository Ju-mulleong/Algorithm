import sys
sys.stdin = open('input.txt', 'r')


'''
완전 이진 트리 아님
자리고정된 인접리스트로 받기
계산은 후위 순회로
'''


def post_order(n):
    # 리프노드라면, 값 바로 return
    if str(adj_lst[n][2]) not in '+-*/':
        return adj_lst[n][2]

    # 연산자라면
    if n <= N:
        left = post_order(adj_lst[n][0])
        right = post_order(adj_lst[n][1])

        if adj_lst[n][2] == '+':
            value_lst[n] = left + right
            return left + right

        elif adj_lst[n][2] == '-':
            value_lst[n] = left - right
            return left - right

        elif adj_lst[n][2] == '*':
            value_lst[n] = left * right
            return left * right

        elif adj_lst[n][2] == '/':
            value_lst[n] = left / right
            return left / right


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 정점의 개수 N

    adj_lst = [[0]*3 for _ in range(N+1)]
    # 정점 번호, 좌 자식, 우 자식, 값
    # 부모 정보는 필요없을듯?

    value_lst = [0]*(N+1)
    for i in range(1, 1+N):
        temp = input().split()
        # 연산자이면
        if temp[1] in '*/-+':
            adj_lst[i][0] = int(temp[2])     # 좌 자식
            adj_lst[i][1] = int(temp[3])     # 우 자식
            adj_lst[i][2] = temp[1]     # 연산자

        # 정수이면(리프)
        else:
            adj_lst[i][2] = int(temp[1])

    # print(adj_lst)
    post_order(1)
    print(f'#{test_case} {int(value_lst[1])}')


