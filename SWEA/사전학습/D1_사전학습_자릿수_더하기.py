'''
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

제약사항 : 자연수 N은 1부터 9999까지의 자연수이다. (1<= N <= 9999)

입력으로 자연수 N이 주어지고, 각 자릿수의 합을 출력해야함.
'''

'''
1. 입력받은 자연수 N을 자릿수별로 합하기. 
    for 사용
'''

num  = input() 
sum = 0

for i in num :      # for에서 in을 문자열로 할 경우, 문자열의 각 문자마다 반복 시행 주의
    sum += int(i)

print(sum)
