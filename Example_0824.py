"""
- 백준 - 스타트와 링크
- URL : https://www.acmicpc.net/problem/14889
"""

import itertools


def solution(cnt, sc):
    # 1. 전체 인원을 두명씩 묶어 조합 딕셔너리 생성
    answer = list()
    num = [x for x in range(cnt)]
    dic = dict()
    for i in num:
        for v in num:
            dic[(i,v)] = score[i][v]+score[v][i]
    
    # 2. 전체 인원의 반씩 묶은 조합 리스트 생성
    c = list(itertools.combinations(num, cnt//2))
    st = list()
    li = list()
    
    # 3. 2에서 묶은 리스트의 반만큼 반복 시작
    for i in range(len(c)//2):
        # 3-1. 2에서 묶은 리스트를 앞에서부터 읽어 두명씩 묶은 리스트로 재생성(스타트팀 조합)
        st = list(itertools.combinations(c[i], 2))
        st_sc = 0
        for a in st:
            st_sc += dic[a]
        
        # 3-2. 2에서 묶은 리스트를 뒤에서부터 읽어 두명씩 묶은 리스트로 재생성(링크팀 조합)
        li = list(itertools.combinations(c[-(i+1)], 2))
        li_sc = 0
        for a in li:
            li_sc += dic[a]
        
        # 3-3. 각 팀 조합 점수 합을 빼서 answer list에 append
        answer.append(abs(st_sc-li_sc))
    
    # 4. 최솟값 print
    print(min(answer))

C = int(input())
score = list()
for i in range(C):
    score.append(list(map(int, input().split(' '))))

solution(C, score)