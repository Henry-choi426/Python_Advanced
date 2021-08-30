"""
- 백준 - 벽 부수고 이동하기
- URL : https://www.acmicpc.net/problem/2206

bfs 활용, 시간초과
"""

def solution(r,m):

    visited = {(x,y):False for x in range(r[0]) for y in range(r[1])}
            
    # que = [x,y,이동한 칸 갯수,벽뚫유무]
    que = list()
    que.append([0,0,1,False])
    target = [r[0]-1,r[1]-1]
    
    while True:
        # que에서 pop해주고 현재 위치를 왔다고 True 표시.
        try:
            x,y,c,b = que.pop()
        except:
            print(-1)
            break
            
        visited[(x,y)] = True
        
        if x == target[0] and y == target[1]:
            print(c)
            break
            
        comb = [(a,y) for a in [x+1,x-1] if a >= 0 and a <= target[0]] + [(x,b) for b in [y+1,y-1] if b >= 0 and b <= target[1]]
        
        # 이미 벽뚫 했으면
        if b:
            # 방문 안하고 벽이 없는 상하좌우를 queue에 append시킴
            for X,Y in comb:
                if visited[(X,Y)] == False and m[X][Y] == 0:
                    que.append([X,Y,c+1,True])
                    
        # 방문 안하고, 벽이 있으면 True, 없으면 False로 상하좌우를 queue에 append시킴
        else:
            for X,Y in comb:
                if visited[(X,Y)] == False:
                    if m[X][Y] == 0:
                        que.append([X,Y,c+1,False])
                    else:
                        que.append([X,Y,c+1,True])
                        

solution(ran,matrix)
                        

ran = list(map(int, input().split(' ')))
matrix = list()
for i in range(ran[0]):
    matrix.append([int(x) for x in input()])

solution(ran,matrix)
