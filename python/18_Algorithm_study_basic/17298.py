# 오큰수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	512 MB	103496	38514	26828	35.210%
# 문제
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

# 출력
# 총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.


import sys
input = sys.stdin.readline

def solution(N, data:list):

###############수정 코드#################
    stack = []
    stack.append(0)
    result = [-1] * N

    for i in range(1, N):
        while stack and data[stack[-1]] < data[i]:
            result[stack.pop()] = data[i]
        stack.append(i)

    print(*result)





###############시간 초과##################

    # for i in range(N):
    #     find = False
    #     for j in range(i, N):
    #         if data[i] < data[j]:
    #             print(data[j], end = ' ')
    #             find = True
    #             break
    #     if not find:
    #         print(-1, end = ' ')



if __name__ == "__main__":
    N = int(input())

    data = list(map(int, input().split()))

    solution(N, data)





