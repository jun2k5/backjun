# 조합 0의 개수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	56153	15975	13170	28.919%
# 문제
#  
# $n \choose m$의 끝자리 
# $0$의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 
# $n$, 
# $m$ (
# $0 \le m \le n \le 2,000,000,000$, 
# $n \ne 0$)이 들어온다.

# 출력
# 첫째 줄에 
# $n \choose m$의 끝자리 
# $0$의 개수를 출력한다.


import sys
input = sys.stdin.readline

def solution(N: int, M: int):
    def count_2(n: int):
        count = 0
        while n > 0:
            n //= 2
            count += n
        return count

    def count_5(n: int):
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

    result = min(count_2(N) - count_2(M) - count_2(N - M), count_5(N) - count_5(M) - count_5(N - M))
    # 0의 개수는 2와 5의 개수 중 작은 값
    print(result)

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)
