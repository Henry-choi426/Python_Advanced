"""
- 백준 -잃어버린 괄호 
- URL : https://www.acmicpc.net/problem/1541

- 풀이 : 
(1) input값 숫자와 기호로 나눠 저장
(2) 뒤에서부터 확인하여 +인 경우를 모아 -인 경우 answer에서 빼주기
(3) 빼주지 않은 값들 마지막에 더하기
"""

C = input()
numbers = list(map(int,C.replace('+',' ').replace('-',' ').split()))
PM = ''.join([i for i in C if not i.isdigit()])

def solution(num,pm):
    answer = num[0]
    r_num = list(reversed(num))
    pm = pm[::-1]
    
    st = 0
    for n,v in zip(r_num,pm):
        if v == '+':
            st += n
        else:
            answer -= st+n
            st = 0
            
    answer += st
    
    print(answer)
        
solution(numbers,PM)