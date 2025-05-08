# 팩토리얼 0의 개수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	101211	47299	39835	46.334%
# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

import sys
input = sys.stdin.readline

def solution(N: int):
    zero_count = 0

    if N == 0 or N == 1:
        print(0)
    else:
        result = 1
        for i in range(2, N + 1):
            result *= i
        if '0' in str(result):
            result = str(result)[::-1]
            for i in result:
                if i == '0':
                    zero_count += 1
                else:
                    break
        print(zero_count)


if __name__ == "__main__":
    N = int(input())
    solution(N)