# 문자열 분석
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	37088	15127	12513	41.245%
# 문제
# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

# 입력
# 첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.

# 출력
# 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        data = input()

        if not data:  # EOF 처리  
            break

        lower = 0
        upper = 0
        digit = 0
        space = -1 # sys.stdin.readline()에서 개행문자를 포함하기 때문에 -1로 초기화

        for char in data:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                space += 1

        print(lower, upper, digit, space)


