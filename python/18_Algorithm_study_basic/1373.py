# 2진수 8진수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	38481	15433	12769	41.508%
# 문제
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.



import sys
input = sys.stdin.readline

def solution(data: str):
    result = ""
    for i in range(len(data), len(data) % 3, -3):
        if i == 0:
            break
        result = str(int(data[i-3:i], 2)) + result
    if len(data) % 3 != 0:
        result = str(int(data[:len(data) % 3], 2)) + result
    print(result)


if __name__ == "__main__":
    data = input().rstrip()
    solution(data)

