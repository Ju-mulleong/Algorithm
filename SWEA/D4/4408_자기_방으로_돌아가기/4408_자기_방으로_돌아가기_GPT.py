import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 개수

for test_case in range(1, 1+T):
    n = int(input())  # 학생 수
    corridor = [0] * 201  # 복도는 1~200번 (방 1~400번)

    for _ in range(n):
        a, b = map(int, input().split())

        # 방 번호를 복도 번호로 변환
        start = (min(a, b) + 1) // 2
        end = (max(a, b) + 1) // 2

        # 해당 복도 구간 카운트 증가
        for i in range(start, end + 1):
            corridor[i] += 1

    # 최댓값이 최소 이동 시간
    print(f'#{test_case} {max(corridor)}')
