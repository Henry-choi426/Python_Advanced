"""
- 백준 - 동전 0
- URL : https://www.acmicpc.net/problem/11047

"""
N, K = list(map(int, input().split(' ')))
p_list = list()
for i in range(N):
    p_list.append(int(input()))
answer = 0
c = K
for i in p_list[::-1]:
    if i <= c:
        answer += c // i
        c = c - ((c // i) * i)
        
print(answer)