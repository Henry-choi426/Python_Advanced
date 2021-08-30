"""
- 코딩테스트 연습 - 2021 KAKAO BLIND RECRUITMENT - 신규 아이디 추천
- URL : https://programmers.co.kr/learn/courses/30/lessons/72410

"""
def solution(new_id):
    data = ''
    answer = ''
    p_list = [str(x) for x in range(10)] + [chr(x) for x in range(97,123)] + ['-','.','_']
    
    # 1. 소문자 치환
    data = new_id.lower()
    now = ''
    for a,i in enumerate(data):
        # 3. 연속. 제거
        if now == '.' and i == '.':
            continue
        
        # 2. 다른 특수문자 제거
        if i in p_list:
            answer += i
            now = i
    
    # 4. 앞뒤 .제거
    while len(answer) > 0:
        if answer[0] != '.' and answer[-1] != '.':
            break
        elif answer[0] == '.':
            answer = answer[1:]
        elif answer[-1] == '.':
            answer = answer[:-1]
    
    # 5,6. 빈 문자열일 경우 a 추가 및 16개 이상일 경우 15개.
    if len(answer) == 0:
        answer += 'a'
    elif len(answer) > 15:
        answer = answer[:15]
        
    while len(answer) > 0:
        print(answer)
        if answer[0] != '.' and answer[-1] != '.':
            break
        elif answer[0] == '.':
            answer = answer[1:]
        elif answer[-1] == '.':
            answer = answer[:-1]
            
            
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer
        
solution("123_.def")