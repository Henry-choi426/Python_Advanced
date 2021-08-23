"""
- 
코딩테스트 연습 - 깊이/너비 우선 탐색(DFS/BFS) - 네트워크
- URL : https://programmers.co.kr/learn/courses/30/lessons/43162
"""

def solution(n, computers):
    answer = 0
    c = [False]*n
    now = 0
    
    for i,v in enumerate(computers):
        # 1. 개인 네트워크인 경우, 갔다는 의미로 true
        if sum(v) == 1:
            c[i] = True
            answer += 1
            
        # 2. 다른것과 연결이 되고 탐색되지 않은 경우, 너비우선탐색 실행
        elif not c[i]:
            q = list()
            
            # 3. 연결된 node를 queue에 추가
            for a,b in enumerate(v):
                if b == 1:
                    q.append(a)
                    
            # 4. 연결된 모든 노드를 탐색할 때 까지 실행
            while len(q) > 0:
                now = q.pop(0)
                
                # 5. 현재 노드가 안가본 곳이면 연결된 노드를 queue에 추가
                if not c[now]:
                    for a,b in enumerate(computers[now]):
                        if b == 1:
                            q.append(a)
                    c[now] = True
                    
            # 6. 노드탐색이 끝나면 하나의 네트워크가 종료됨을 의미하므로 +1
            answer += 1
            
    return answer
solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])