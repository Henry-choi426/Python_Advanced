"""
- 코딩테스트 연습 - 2021 KAKAO BLIND RECRUITMENT - 합승 택시 요금
- URL : https://programmers.co.kr/learn/courses/30/lessons/72413

- 정확성 테스트 통과(50점), 효율성 테스트 30점
"""
def cube(x):
    x[0], x[1] = x[0]-1, x[1]-1
    return x

def solution(n, s, a, b, fares):
    answer = 0
    fares = list(map(cube, fares))
    s -= 1
    a -= 1
    b -= 1
    
    costs = {x:[] for x in range(n)}
    for S in range(n):
        
        visited = [False for _ in range(n)]
        cost = [20000001 for _ in range(n)]
        
        visited[S] = True
        cost[S] = 0
        checkLoc = S
        
        # 현 위치에서 다음 위치까지의 비용.
        for v1, v2, c in fares:
            if v1 == checkLoc and visited[v2] == False:
                cost[v2] = min(cost[v2],cost[v1]+c)
            if v2 == checkLoc and visited[v1] == False: #
                cost[v1] = min(cost[v1],cost[v2]+c)

        # 방문하지 않은 노드가 있다면 방문하지 않은 지역중 최솟값 찾기.
        while False in visited:
            checkLoc = -1
            CheckValue = 500001

            # 방문하지 않은 지역 중 최솟값 찾기
            for i in range(n):
                if visited[i] == False and cost[i] < CheckValue:
                    checkLoc = i
                    CheckValue = cost[i]

            # 방문하지 않은 지역이 없으면 while문 탈출
            if checkLoc == -1:
                break

            # 해당 지역에서의 최솟값 추출
            visited[checkLoc] = True
            for v1, v2, c in fares:
                if v1 == checkLoc and visited[v2] == False:
                    cost[v2] = min(cost[v2], cost[v1]+c)
                if v2 == checkLoc and visited[v1] == False:
                    cost[v1] = min(cost[v1], cost[v2]+c)
                    
        costs[S] = cost
    last = list(costs.values())
    answer = 2000000000
    for i,v in enumerate(last):
        answer = min(v[a]+v[b]+last[s][i],answer)
        
    return answer