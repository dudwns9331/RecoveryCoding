# 줄번호 백준 23795 파이썬 기본문법 배우기
# 입력한 값은 2000개 미만, 총 합을 출력한다.

import sys

input = lambda: sys.stdin.readline().rstrip()

result = 0

while True:
    number = int(input())
    if number == -1:
        break
    else:
        result = result + number
print(result)

"""
while 문을 통한 무한 반복
파이썬에서 for 문은 반복문을 의미하지만 유한한 범위 내에서 가능하다.
정해진 조건이 아닌 불특정한 조건을 통해서 반복문을 실행하고 싶으면 while 을 써야한다.
파이썬에서 boolean 변수는 True, False 등 대문자로 사용한다.
if 문은 괄호 없이 : 콜론으로 마무리한다.
"""
