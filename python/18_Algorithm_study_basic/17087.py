# 숨바꼭질 6
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	12626	6379	5124	49.536%
# 문제
# 수빈이는 동생 N명과 숨바꼭질을 하고 있다. 수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.

# 수빈이는 걸어서 이동을 할 수 있다. 수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.

# 모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 105)과 S(1 ≤ S ≤ 109)가 주어진다. 둘째 줄에 동생의 위치 Ai(1 ≤ Ai ≤ 109)가 주어진다. 동생의 위치는 모두 다르며, 수빈이의 위치와 같지 않다.

# 출력
# 가능한 D값의 최댓값을 출력한다.


import sys 
from math import gcd
input = sys.stdin.readline

def solution(N: int, S: int, data: list):
    # 수빈이의 위치 S와 동생들의 위치 A1, A2, ..., AN이 주어졌을 때,
    # 가능한 D의 최댓값을 구하는 방법
    # 1. 수빈이의 위치 S와 동생들의 위치 A1, A2, ..., AN의 차이를 구한다.
    # 2. 차이의 GCD를 구한다.
    # 3. GCD를 출력한다.
    
    data = [abs(S - x) for x in data]
    result = data[0]
    
    for i in range(1, N):
        result = gcd(result, data[i])
    
    print(result)

if __name__ == "__main__":
    N, S = map(int, input().split())
    data = list(map(int, input().split()))
    solution(N, S, data)