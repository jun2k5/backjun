# GCD 합 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	39843	16057	13206	43.022%
# 문제
# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

# 출력
# 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.


import sys
from math import gcd
input = sys.stdin.readline

def solution(n: int, data: list):
    # GCD의 합을 구하는 방법
    # 1. 모든 쌍의 GCD를 구한다.
    # 2. GCD의 합을 구한다.
    # 3. 결과를 출력한다.
    
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            result += gcd(data[i], data[j])
    
    print(result)

if __name__ == "__main__":
    dataN = int(input())
    for _ in range(dataN):
        data = list(map(int, input().split()))
        n = data[0]
        data = data[1:]
        solution(n, data)