import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 도감에 수록되어 있는 포켓몬의 개수 N, 문제의 개수 M

# 빠른 탐색 위해 딕셔너리 사용

dogam = {}
for i in range(1, N+1):
    dogam[i] = input().strip()

# 역방향 딕셔너리 만들기
reverse_dogam = {v: k for k, v in dogam.items()}


# 이제 문제 입력받음, 숫자(도감번호) 입력받으면 포켓몬 이름, 포켓몬 이름 입력받으면 도감번호 출력
# 저번에 했던것처럼 리스트안에 다 때려놓고, 출력은 한 번만
ans = []
# print(dogam)

# 당연히 입력받을때는 문자열이지만, 정수로 변환할수있는 '숫자'를 판별하는 함수
# isdigit()

for i in range(M):
    temp = input().strip()
    # print(temp)
    if temp.isdigit():
        ans.append(dogam[int(temp)])
    else:
        ans.append(reverse_dogam[temp])

print(*ans, sep='\n')



'''
도감번호와 문제 개수가 1이상 10만 이하,
리스트의 index()는 시간복잡도가 O(N)이다. 
빈번한 탐색이 필요할경우 딕셔너리나 집합 사용

특정 딕셔너리에서 value가 중복되지 않음이 보장될때, 역방향 딕셔너리를 만드는게 가장 효율적이다.
'''