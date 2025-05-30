# 나머지 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	473288	241622	207294	51.205%
# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

import sys
input = sys.stdin.readline


def solution(A: int, B: int, C: int) -> None:
    print((A + B) % C)
    print(((A % C) + (B % C)) % C)
    print((A * B) % C)
    print(((A % C) * (B % C)) % C)



if __name__ == "__main__":
    A, B, C = map(int, input().split())
    solution(A, B, C) 
