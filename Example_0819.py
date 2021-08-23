"""

코딩테스트 연습 - 정렬 - K번째수
- URL : https://programmers.co.kr/learn/courses/30/lessons/42748
"""

def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer