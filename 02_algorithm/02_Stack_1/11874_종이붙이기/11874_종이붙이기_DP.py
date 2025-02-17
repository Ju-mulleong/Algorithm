import sys
sys.stdin = open('inpu.txt', 'r')

T = int(input())
m = [1, 1]
for i in range(2, 31):
    m.append(m[i-1] + 2 * m[i-2])

for tc in range(1, T+1):
    N = int(input()) // 10
    print(f'#{tc} {m[N]}')