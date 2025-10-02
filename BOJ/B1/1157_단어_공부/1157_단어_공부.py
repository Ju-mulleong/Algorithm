# import sys

# sys.stdin = open("input.txt", "r")

"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내기
단, 가장 많이 사용된 알파벳이 복수일경우, '?'를 출력한다.

대문자와 소문자를 구분하지 않으므로, 둘 중 하나로 통일해서 변환시키기
JS는 toUpperCase였나 그거였는데 python은?

문자열 메서드, s.upper() 또는 s.lower()

"""

# T = 4

# for test_case in range(T):
str = input().upper()  # 대문자로 통일
len_str = len(str)
ans = str[0]

dict_str = dict()

# 알파벳 사용할때마다 dict
for i in range(len_str):
    k = str[i]
    if k in dict_str.keys():
        dict_str[k] += 1
    else:
        dict_str[k] = 1

# dict에서 value가 최대인 key 찾기

lst_dict = dict_str.values()
set_dict = set(lst_dict)
# print(lst_dict)

slst_dict = sorted(lst_dict, reverse=True)

if len(slst_dict) != 1 and slst_dict[0] == slst_dict[1]:
    print("?")

else:
    for s in str:
        if dict_str[s] == max(lst_dict):
            print(s)
            break
