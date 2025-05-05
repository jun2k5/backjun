# 최대공약수와 최소공배수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	134128	77555	63196	57.651%
# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.


import sys
from math import gcd, lcm
input = sys.stdin.readline



def solution(A: int, B: int):
    print(gcd(A, B)) # 최대공약수
    print(lcm(A, B)) # 최소공배수

if __name__ == "__main__":
    A, B = map(int, input().split())
    solution(A, B)