"""
- 백준 -숨바꼭질
- URL : https://www.acmicpc.net/problem/1697

- 풀이 : 
(1) input값 숫자로 저장
(2) 최대값 지정 및 list 생성
(3) 조건에 맞는 경우 큐에 추가하여 값 찾기.
"""
from collections import deque

def solution1(st, en):
    q = deque()
    MAX = 10**5
    dist = [0] * (MAX+1)
    q.append(st)
    
    while True:
        now = q.popleft()
        if now == en:
            print(dist[now])
            break
        else:
            for i in [now+1,now-1,now*2]:
                if 0 <= i <= MAX and not dist[i]:
                    q.append(i)
                    dist[i] = dist[now]+1
            
C = list(map(int, input().split(' ')))
solution1(C[0], C[1])