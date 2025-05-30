# 2×n 타일링
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	206693	80510	59770	36.906%
# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.


import sys
input = sys.stdin.readline

def solution(n: int) -> int:
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[n])

if __name__ == "__main__":
    n = int(input())
    
    solution(n)