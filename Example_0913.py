"""
코딩테스트 연습 - 동적계획법(Dynamic Programming) - 도둑질
URL : https://programmers.co.kr/learn/courses/30/lessons/42897

문제 설명
- 맨 끝집과 첫 집이 연결되어 있고, 이웃된 두 집을 털 수 없으니
    1. 첫 집을 터는 경우
    2. 마지막 집을 터는 경우
로 나눠 각각의 경우의 최댓값을 answer에 append한다.

- 각 집마다의 최댓값을 구하는 로직 (4번째 집 기준)
    1. 첫번째집에서의 최댓값 + 세번째 집에서의 money
    2. 첫번째집에서의 최댓값 + 네번째 집에서의 money
    3. 두번째집에서의 최댓값 + 네번째 집에서의 money
중 최댓값이다.
"""


def solution(money):
    answer = list()
    for a in range(2):
        max_money = [0 for _ in range(len(money))]
        if a:
            max_money[0] = money[0]
        max_money[1] = max(money[1],max_money[0])
        max_money[2] = max(money[2]+max_money[0],max_money[1])
        for i in range(3,len(money)-a):
            max_money[i] = max(max_money[i-3]+money[i-1],max_money[i-3]+money[i],max_money[i-2]+money[i])
        answer.append(max(max_money))
    return max(answer)

solution([0,99,99, 1, 1,1,1,1,99,0])