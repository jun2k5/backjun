# 8진수 2진수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	53467	18421	15417	36.367%
# 문제
# 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.

# 출력
# 첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.


import sys
input = sys.stdin.readline

def solution(data: str):
    result = ""
    for i in data:
        result += str(bin(int(i, 8)))[2:].zfill(3)
    print(result.lstrip('0') or '0')
#
if __name__ == "__main__":
    data = input().rstrip()
    solution(data)