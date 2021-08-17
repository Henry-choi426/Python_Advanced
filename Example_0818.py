"""
- 백준 -  N과 M (2)
- URL : https://www.acmicpc.net/problem/15650
"""

import itertools

def solution(a,b):
    l = [i for i in range(1,a+1)]
    for i in itertools.combinations(l,b):
        for v in i:
            print(v,end=' ')
        print()

C = list(map(int, input().split(' ')))
solution(C[0],C[1])