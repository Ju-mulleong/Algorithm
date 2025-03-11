# 전선 N개
#   - 교차점 발생
#   - 몇 개 발생하는 지 COUNT
#
# ----------------------- 문제 읽기
#
# 교차점은 무슨 조건일 때 발생할까 ?
# - 새로운 선을 추가할 때 (교차점이 발생하는 케이스)
#   -> 새로운 선 추가할 때 마다 비교를 진행
#   - 기존 선과 비교
#     [검증] 시간적으로 매우 여유롭다
# 	(모두 최악(1000번)으로 가정해도 1,000,000번)
#     -> 기존선 들을 저장하면서 진행
#     - 1. 시작점이 높으며, 도착점이 낮음
#     - 2. 시작점이 낮으며, 도착점이 높음
#
# ----------------------- 설계

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())        # 선의 개수

    # 1. N개의 새로운 선을 추가하면서 비교를 진행
    #   기존 선들을 저장하면서 진행
    # 2. 비교 = 기존 선들과 비교
    wires = []          # 기존 선들을 저장할 리스트
    answer_count = 0    # 교차점 수

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존 연결된 선들과 비교
        for prev_start, prev_end in wires:
            # 교차점 조건1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
            if start > prev_start and end < prev_end:
                answer_count += 1

            # 교차점 조건2. 기존의 전선보다 시작점이 낮고, 도착점이 높다
            if start < prev_start and end > prev_end:
                answer_count += 1

        # 목록에 전선을 추가
        wires.append((start, end))
    print(f'#{tc} {answer_count}')




