"""
- 백준 - 태권왕
- URL : https://www.acmicpc.net/problem/14562

- 풀이 : 
(1) input값 int화 후 함수에 넣기
(2) queue를 활용한 bfs(너비우선탐색) 실행
(3) s,t 값이 같아지면 return
"""

def bfs(S, T):
    q = list()
    q.append([S,T,0])
    while True:
        s, t, c = q.pop(0)
        if s <= t:
            q.append([s*2,t+3,c+1])
            q.append([s+1,t,c+1])
            if s == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))