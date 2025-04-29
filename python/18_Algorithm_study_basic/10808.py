# 알파벳 개수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	63965	43433	34192	68.116%
# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

import sys
input = sys.stdin.readline


def solution(data: list):
    count = [0] * 26  # 알파벳 개수 초기화

    for char in data:
        count[ord(char)-ord('a')] += 1

    print(*count)

if __name__ == "__main__":

    data = list(input().rstrip())
#    print(data)

    solution(data)
