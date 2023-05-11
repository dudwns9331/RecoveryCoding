# 치킨 두마리 백준 14489번 파이썬 기본문법 배우기
# 처음에는 통장 잔고의 값, 두번째는 치킨 한마리의 가격

import sys

input = lambda: sys.stdin.readline().rstrip()

account1, account2 = map(int, input().split())

chickenPrice = int(input()) * 2

if account1 + account2 >= chickenPrice:
    print(account1 + account2 - chickenPrice)
else:
    print(account1 + account2)
