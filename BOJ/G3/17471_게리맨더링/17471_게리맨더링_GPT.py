import sys
sys.stdin = open('input4.txt', 'r')


def is_connected(n, graph, group):
    """ BFS를 사용하여 group 내의 노드들이 모두 연결되어 있는지 확인 """
    visited = []  # 방문한 노드를 저장할 리스트
    queue = [group[0]]  # BFS를 위한 큐, 초기값으로 그룹의 첫 번째 노드 삽입
    visited.append(group[0])

    while queue:
        node = queue.pop(0)  # 큐에서 맨 앞의 노드 꺼내기
        for neighbor in graph[node]:  # 현재 노드의 이웃 탐색
            if neighbor in group and neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return len(visited) == len(group)  # 방문한 노드 수가 그룹 크기와 같으면 연결된 것


def min_population_difference(n, populations, graph):
    min_diff = 1000000  # 최소 차이를 저장할 변수, 큰 값으로 초기화
    total_population = 0
    for pop in populations:
        total_population += pop  # 전체 인구 계산

    # 가능한 모든 크기의 선거구 조합을 탐색 (1개 이상 n//2 이하)
    for size in range(1, n // 2 + 1):
        possible_combinations = []  # 모든 조합을 저장할 리스트
        stack = [[i] for i in range(n)]  # 초기 조합을 위해 모든 노드를 개별적으로 리스트로 넣음

        while stack:
            subset = stack.pop()
            if len(subset) == size:
                possible_combinations.append(subset)
                continue
            last = subset[-1]  # 현재 부분집합의 마지막 원소
            for i in range(last + 1, n):  # 오름차순으로 부분집합 생성
                stack.append(subset + [i])

        for group_a in possible_combinations:
            group_b = []
            for i in range(n):
                if i not in group_a:
                    group_b.append(i)

            if is_connected(n, graph, group_a) and is_connected(n, graph, group_b):
                pop_a = 0
                for i in group_a:
                    pop_a += populations[i]
                pop_b = total_population - pop_a
                diff = abs(pop_a - pop_b)
                if diff < min_diff:
                    min_diff = diff

    return min_diff if min_diff != 1000000 else -1


# 입력 처리
n = int(input())
populations = []
temp = input().split()
for t in temp:
    populations.append(int(t))

graph = []
for i in range(n):
    graph.append([])
    data = input().split()
    for j in range(1, len(data)):
        graph[i].append(int(data[j]) - 1)  # 0-index 변환

# 결과 출력
print(min_population_difference(n, populations, graph))
