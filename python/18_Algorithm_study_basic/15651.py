# N과 M (3)
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	84884	56647	41968	66.809%
# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

import sys
input = sys.stdin.readline

def solution(n: int, m: int) -> None:
    def dfs(start: int, path: list) -> None:
        if len(path) == m:
            print(" ".join(map(str, path)))
            return

        for i in range(1, n+1):
            dfs(i, path + [i])

    dfs(1, [])

if __name__ == "__main__":
    n, m = map(int, input().split())
    solution(n, m)