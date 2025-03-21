# 10950문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

def solution():
    #입력
    T = int(input())
    
    #T만큼 A, B입력받고 A+B 출력하는 For문
    for i in range(0, T):
        A, B = map(int, input().split())
        print(A + B)

if __name__ == "__main__":
    solution()

"""
-Learning Point
단순하게 생각하고
단순한 코드를 짜보자.

"""

