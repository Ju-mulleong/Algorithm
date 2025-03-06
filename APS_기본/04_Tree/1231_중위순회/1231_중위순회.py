import sys
sys.stdin = open('input.txt', 'r')


'''
주어진 트리를 in-order형식으로 순회(중위순회)
완전 이진트리 형식으로 주어진다.
어차피 완전이진트리로 주어지고 심지어 순서대로 준다.
주는 인풋중에 글자만 순서대로 저장
'''


def in_order(n):
    global string
    # print(n)
    if n <= N:
        in_order(n*2)
        string += adj_lst[n]
        in_order(n*2+1)


T = 10

for test_case in range(1, 1+T):
    N = int(input())

    adj_lst = [0]*(1+N)

    for i in range(1, N+1):
        adj_lst[i] = input().split()[1]

    string =""
    # print(adj_lst)

    in_order(1)
    print(f'#{test_case} {string}')
