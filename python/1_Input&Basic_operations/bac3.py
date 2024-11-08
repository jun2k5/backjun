# 10869번 문제
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.


def solution():
    A, B = map(int, input().split())
    print(A+B)
    print(A-B)
    print(A*B)
    print(int(A/B))
    print(A%B)


if __name__ == "__main__":
    solution()

"""
-Learning Point
    A / B 는 기본적으로 float타입으로 반환되어
    원하는 결과값을 형변환으로 얻어낼 것.    
"""