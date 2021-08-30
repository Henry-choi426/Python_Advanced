"""
- 코딩테스트 연습 - 2021 KAKAO BLIND RECRUITMENT - 순위 검색
- URL : https://programmers.co.kr/learn/courses/30/lessons/72412

- 효율성 테스트 통과 못함
"""
def solution(info, query):
    people = len(info)
    info_np = list()
    q_np = list()
    answer = []
    
    for i in info:
        info_np.append(list(i.split(' ')))
    for i in query:
        q_np.append(list(i.replace('and','').replace('  ',' ').split(' ')))
    
    for a in q_np:
        test = list()

        if a[-1] != '-':
            test = list(filter(lambda x : int(x[4]) >= int(a[4]),info_np))
        else:
            test = info_np.copy()
        people = 0

        for b in test:
            for c in range(4):
                if a[c] == '-':
                    pass
                elif a[c] != b[c]:
                    break
                if c == 3:
                    people += 1
        answer.append(people)

    return answer