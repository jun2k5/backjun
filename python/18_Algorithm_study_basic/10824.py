# 네 수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	33889	15529	13626	46.220%
# 문제
# 네 자연수 A, B, C, D가 주어진다. 이때, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.

# 두 수 A와 B를 합치는 것은 A의 뒤에 B를 붙이는 것을 의미한다. 즉, 20과 30을 붙이면 2030이 된다.

# 입력
# 첫째 줄에 네 자연수 A, B, C, D가 주어진다. (1 ≤ A, B, C, D ≤ 1,000,000)

# 출력
# A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.


def solution(A:int , B:int, C:int, D:int):
    AB = str(A) + str(B)
    CD = str(C) + str(D)
    AB = int(AB)
    CD = int(CD)    
    print(AB + CD)



if __name__ == "__main__":
    A, B ,C, D = map(int, input().split())
    
    solution(A, B, C, D)