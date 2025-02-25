import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
쿼터(0.25), 다임(0.1), 니켈(0.05), 페니(0.01)
로 거스름돈의 조합을 만든다. 
단, 거스름돈의 개수가 가장 적은 조합

굳이 부분집합 쓸 필요도 없이 쿼터로 최대한 채우고, 다임 채우고, 니켈 채우고.. 하면 될 듯

거스름돈을 센트로 준다. 그냥 25, 10, 5, 1로 생각해도 된다.
'''

for test_case in range(1, 1+T):
    C = int(input())        # 줘야하는 거스름돈

    ans = []
    for i in [25, 10, 5, 1]:
        ans.append(f'{C // i}')      # 몫 리스트에 추가
        C = C % i     # 큰 단위부터 순서대로 거스름돈 걸러내기

    print(" ".join(ans))