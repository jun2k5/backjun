# 10951문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

import sys

def solution():

    #A, B값을 게속 받아들이는 while문
    while 1:

        try:
            #입력            
            A, B = map(int, sys.stdin.readline().split())
            #A + B값 출력         
            sys.stdout.write(f"{A + B}" + "\n")
            
        except:
            break
    

if __name__ == "__main__":
    solution()


"""
-Learning Point
while + 상수값 조합으로 무한루프 while문을 만들 수 있다.
이때 try-except문으로 오류처리를 안해주면 런타임 에러가 발생한다.
"""