# 사탕 게임 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	55873	20118	13774	34.716%
# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.


import sys
input = sys.stdin.readline

def solution(bord:list, n: int):
    max_candies = 0

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 방향

    def count_candies():
        nonlocal max_candies
        for i in range(n):
            # Count horizontal candies
            count = 1
            for j in range(1, n):
                if bord[i][j] == bord[i][j - 1]:
                    count += 1
                else:
                    max_candies = max(max_candies, count)
                    count = 1
            max_candies = max(max_candies, count)

            # Count vertical candies
            count = 1
            for j in range(1, n):
                if bord[j][i] == bord[j - 1][i]:
                    count += 1
                else:
                    max_candies = max(max_candies, count)
                    count = 1
            max_candies = max(max_candies, count)     
    
    count_candies()

    for i in range(n):
        for j in range(n):
            for dx, dy in d:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    # Swap candies
                    bord[i][j], bord[ni][nj] = bord[ni][nj], bord[i][j]
                    count_candies()
                    # Swap back
                    bord[i][j], bord[ni][nj] = bord[ni][nj], bord[i][j]

    print(max_candies)

    

if __name__ == "__main__":
    n = int(input().strip())
    board = [list(input().strip()) for _ in range(n)]
    
    solution(board, n)