import sys
sys.stdin = open('input.txt', 'r')

# B진법수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램 작성
# A:10, B:11, C:12.... Z:35
# 이걸 미리 딕셔너리처럼 지정해줘야하나? 
# 아니면 A 다음은 B 라는걸 파이썬에서 인식할 수 있는 기능이 있나
# 일단 알파벳으로 이루어진 list만들고, 그 인덱스에 +10해서 값으로 하면 조건 만족할듯

alphabet_list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    ]

target_num, N = input().split()
N = int(N)

# N^0, N^1...을 target_num에서 한 글자씩 떼어서 문자면 해당하는 숫자를 할당한 뒤, 계수처럼 곱하면 될듯

sum_value = 0
cnt = 0
for i in target_num[::-1]:      # 이거 되나? 문자열도 슬라이싱 되네?
    # in으로 True 라면 그 글자의 index+10을 계수로 재할당
    if i in alphabet_list:
        k = alphabet_list.index(i) + 10

    else :
        k = int(i)
    
    sum_value += k * N ** (cnt)
    cnt += 1

print(sum_value)