"""
- 코딩테스트 연습 - 탐욕법(Greedy) - 단속카메라
- URL : https://programmers.co.kr/learn/courses/30/lessons/42884

"""
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치 찾기

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
