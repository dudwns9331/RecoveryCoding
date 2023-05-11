# 줄번호 백준 4470 파이썬 기본문법 배우기

import sys

# lambda 는 함수로 만들어준다. 람다식에 대해서 생각해보기
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for i in range(1, n+1):
    result = input()
    # 파이썬에서 형식 포멧?
    print(f"{i}. {result}")

"""
sys.stdin : 표준 입력
sys.stdout : 표준 출력
sys.stderr : 표준 에러

sys.stdin.readline().rstrip() 은 공백 없이 입력을 받는다.
n = int(input) 은 입력받은 str을 정수로 변환한다.

for 변수 in range(시작 값, 끝값) :
    result = input().rstrip()


"""