# 영수증 백준 24304번 파이썬 기본문법 배우기
# 처음에 입력한 값은 영수증의 값, 두번째 값은 물품의 개수

import sys

input = lambda: sys.stdin.readline().rstrip()

result = int(input())
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    result = result - (a * b)

if result == 0:
    print("Yes")
else:
    print("No")

"""
map은 2개의 값을 받을 때? 사용한다?
map(function, iterable)
첫번째는 매개변수로 함수, 두번째는 반복 가능한 자료형(리스트, 튜플 등)
"""