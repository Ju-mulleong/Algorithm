import sys
sys.stdin = open('input1.txt', 'r')     # input1.txt, input2, input3

'''
자신의 키를 알 수 있다
     모든 노드들과 닿을 수 있다? 아닌듯
     1번은 3번과의 키 비교 불가
     
     자신을 통과해서 모든 노드를 단방향으로 탐색 가능할 때?
     4번 기준으로 1,3,5가 자신을 통해서 들어오고 / 2,6번으로 나갈 수 있다.
     
     5번은 1번보다 크고 2,4,6이 자기보다 크지만 3번 파악 불가
     
    
'''
