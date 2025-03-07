import sys
sys.stdin = open('input.txt', 'r')
# 표준 입력에 input.txt를 일기모드로 열어서 할당

sys.stdout = open('output.txt', 'w')
# 표준 출력에 output.txt를 쓰기모드로 열어서 할당


a, b = map(int, input().split())
print(a, b)