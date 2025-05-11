# 소수 구하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	315660	96924	68067	28.548%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys
import math
input = sys.stdin.readline 

def solution(M: int, N: int):
    # 에라토스테네스의 체
    # 1. 2부터 N까지의 모든 수를 소수로 초기화한다.
    # 2. 2부터 N의 제곱근까지의 수를 반복한다.
    # 3. 현재 수가 소수인 경우, 그 배수를 모두 소수가 아니라고 표시한다.
    # 4. M 이상 N 이하의 소수를 출력한다.
    
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False

    for i in range(M, N + 1):
        if is_prime[i]:
            print(i)
            
if __name__ == "__main__":
    M, N = map(int, input().split())
    solution(M, N)