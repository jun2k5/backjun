# 10952문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 입력의 마지막에는 0 두 개가 들어온다.

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

import sys

def solution():
    #상태 변수 Go 선언
    Go = True

    #A, B값을 게속 받아들이는 while문
    while Go:
        #입력
        A, B = map(int, sys.stdin.readline().split())
        #만약 A와 B의 값이 모두 0이면
        if A == 0 and B == 0:
            #멈춤
            Go = False
            #마지막에 A+B출력 막는 break함수
            break

        #A + B값 출력
        sys.stdout.write(f"{A + B}" + "\n")
    

if __name__ == "__main__":
    solution()


"""
-Learning Point
break문으로 루프문을 탈출할 수 있다.
print문에서 f"{function()}"으로 변수값이나 함수, 연산을 출력할 수 있다.
"""