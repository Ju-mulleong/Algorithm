import sys

sys.stdin = open("input.txt", "r")

"""
SWEA에서 했던 괄호문제.
짝 맞추기

그때 어떻게 했었는지는 기억안나는데 일단 생각나는대로 먼저 풀어보고 예전꺼 보기
"""

T = int(input())


for test_case in range(T):
    temp = input()
    L = len(temp)
    cnt = 0
    flag = 0

    # 그냥 반복문으로 처리?
    # 왼쪽이 없는데, 오른쪽게 나오는 순간 NO
    for i in range(L):
        if temp[i] == "(":
            cnt += 1
        elif temp[i] == ")":
            cnt -= 1
        if cnt < 0:
            flag = 1
            break

    if flag == 0 and cnt == 0:
        print("YES")
    else:
        print("NO")
