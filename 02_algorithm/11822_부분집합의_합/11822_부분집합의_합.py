import sys
sys.stdin = open('input.txt', 'r')

# 비트 연산자 사용

T = int(input())    # 테스트 케이스의 수 T

# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K

# 집합에서 원소들의 합 구하는 함수 선언


def SumOfelements(lst):
    sum_e = 0
    for i in lst:
        sum_e += i
        return sum_e


for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    # print(N, K)

    # 부분 집합 중 N개의 원소를 가진 집합들 다 정렬.
    # 그 집합들 각각의 원소들의 합이 K와 같은 부분집합 개수 cnt
    # 해당하는 부분집합 없는 경우 0 출력







