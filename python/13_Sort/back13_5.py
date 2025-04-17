# 수 정렬하기 3 언어 제한
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 5 초 (하단 참고)	8 MB (하단 참고)	345433	83145	63545	23.950%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    result = [0] * 10001

    for i in range(N):
        result[int(input())] += 1

    for j in range(len(result)):
        if result[j] != 0:
            for k in range(result[j]):
                print(j)









#===================# #메모리 초과# #============================
# import sys
# input = sys.stdin.readline


# def solution(N:int, data:list):
#     data.sort()

#     for i in range(N):
#         print(data[i])
    


# if __name__ == "__main__":
#     N = int(input())
#     data = [int(input()) for _ in range(N)]

#     solution(N, data)





