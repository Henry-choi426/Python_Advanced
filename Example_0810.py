"""
- 코딩테스트 연습 - 탐욕법 - 섬 연결하기
- URL : https://programmers.co.kr/learn/courses/30/lessons/42861

- 풀이 : 
(1) set자료구조에 출발, 도착 지점을 추가해주고 
-> 중복을 제거해야하기 때문에 set자료구조를 사용
(2) answer에 비용을 추가하고 -> 우리가 원하는 정답
(3) 사용한 Routes를 제거
"""

def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    routes = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    
    while n != len(routes):
        for i, v in enumerate(costs[1:]):
            if v[0] in routes and v[1] in routes:
                continue
                
            if v[0] in routes or v[1] in routes:
                routes.update([v[0], v[1]])
                answer += v[2]
                costs.pop(i+1)
                break
        
    return answer

solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
# 4