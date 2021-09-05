"""
- 코딩테스트 연습 - 깊이/너비 우선 탐색(DFS/BFS) - 단어 변환
- URL : https://programmers.co.kr/learn/courses/30/lessons/43163
"""
def solution(begin, target, words):
    
    # words 속 target 값 없는 경우 0 반환
    if not target in words:
        return 0
    
    # 하나만 다른 경우를 찾기위한 상수
    length = len(begin) - 1
    stack = []
    stack.append([begin,0])
    
    while stack:
        now = stack.pop()
        
        # 현재 단어가 타겟 단어와 같다면 결과 return
        if now[0] == target:
            return now[1]
        
        # 현재 단어와 words 속 단어가 한 글자만 다른 경우 stack과 remove_list에 append
        remove_list = []
        for word in words:
            if length == sum(list(map(lambda x,y : x==y,list(now[0]),list(word)))):
                stack.append([word,now[1]+1])
                remov.append(word)
                
        # words 중 사용한 단어는 remove_list 활용하여 제거.
        for re in remove_list:
            words.remove(re)
    
    # words를 다 돌았는데 target값과 매칭이 안된 경우 0 반환
    return 0

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])