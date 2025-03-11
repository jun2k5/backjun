# 8389문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

def solution():
    #입력
    n = int(input())
    #결과값 초기화
    result = 0

    #1부터 N까지 합 For문
    for i in range(1, n+1):
        result += i

    #출력
    print(result)

if __name__ == "__main__":
    solution()

"""
-Learning Point
range(A,B)함수는 A부터 B-1까지의 범위를 반환한다.
"""

