import sys
import string   # 알파벳을 쉽게 가져올 수 있는 상수가 포함된 라이브러리
sys.stdin = open('input.txt', 'r')


# print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

abc_list = list(map(lambda x: x, string.ascii_uppercase))
# print(abc_list)
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
#  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num, B = map(int, input().split())

# 10진법 수 num을 B진법으로 출력

'''
어떤 임의의 수 num을 B진수로 나타내려면
이진법이라면 계속 나눠서 나머지를 기록하는 식인데
36진법이라도 비슷하게 하면 될듯?
    1. 인덱스를 지수로 하고 0에서 1씩증가.
    2. 예를 들어 B가 36이라면, for문으로 돌려서 36으로 돌렸을때 몫과 나머지 구함.
    3. 나머지를 ans에 append하고 몫을 다시 이 과정을 반복
    4. 적고보니까 재귀함수인 것 같다.
    5. 함수쓰다보니까 재귀가 아니라 while이 더 깔끔할것같기도 하고?
'''

# 나눌 값을 계속 반복하면서 할당(몫으로)
# 이 값이 B보다 적어질 때 까지 반복
# 출력값은 숫자+문자니까 str이여야함!!!!!!

ans = ''
while num >= B:
    r = num % B

    if r > 9:  # 만약 나머지가 9보다 크다면 (10진법 체계내 0~9로 나타낼 수 없다면)
        r = abc_list[r-10]  # abc_list에서 해당하는 글자 재할당
        ans += r    # 출력값 문자열에 나머지 더하기 (str(str)) 안 하기위해 따로 구분
    
    else :
        ans += str(r)    # 출력값 문자열에 나머지 더하기
    
    num = num // B      # 몫 다시 나눌 값에 할당
    
# 반복을 다 끝내고 남은 수(num)도 넣어야됨.
r = num     # 위의 코드와 혼동 방지용 변수 할당

if r > 9:
    r = abc_list[r-10]
    ans += r

else:
    ans += str(r)
    
ans = ans[::-1]     # 거꾸로 재할당
print(ans)