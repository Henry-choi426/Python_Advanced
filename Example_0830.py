"""
- 코딩테스트 연습 - 2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼
- URL : https://programmers.co.kr/learn/courses/30/lessons/72411

"""
import itertools
def solution(orders, course):
    answer = []
    comb = dict()
    cnt = dict()

    comb = {x:[] for x in course}
    
    for c in course:
        for order in orders:
            if len(order) >= c:
                comb[c].append(list(itertools.combinations(order,c)))
    
    for a in comb.values():
        for b in a:
            for c in b:
                d = ''.join(sorted(c))
                if cnt.get(d):
                    cnt[d] += 1
                else:
                    cnt[d] = 1
    
    comb = {x:[] for x in course}
    comb_max = {x:0 for x in course}
    for i,v in list(cnt.items()):
        if v > 1:
            if v > comb_max[len(i)]:
                comb[len(i)] = [i]
                comb_max[len(i)] = v
            elif v == comb_max[len(i)]:
                comb[len(i)].append(i)
        
    for i in comb.values():
        for v in i:
            answer.append(v)
            
    return sorted(answer)