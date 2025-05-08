# 팩토리얼
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	189135	105294	86832	55.917%
# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

import sys
input = sys.stdin.readline

def solution(N: int):
    if N == 0 or N == 1:
        print(1)
    else:
        result = 1
        for i in range(2, N + 1):
            result *= i
        print(result)

if __name__ == "__main__":
    N = int(input())
    solution(N)