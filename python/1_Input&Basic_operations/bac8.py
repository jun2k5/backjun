# 11382문제
# 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

# 입력
# 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

# 출력
# A+B+C의 값을 출력한다.

# def solution():
#     A, B, C = map(int, input().split())
#     print(A + B + C)

import sys

def solution():
   A = map(int, input().split())
   print(A)
#   A = sys.stdin.readline()
#   print(type(A))


if __name__ == "__main__": 
    solution()




"""
-Learning Point
    python에서는 자동 형변환( Auto Casting )을 지원하기때문에 따로 고려하지 않아도 괜찮지만
    sys.stdin.readline() -> str타입 반환
    map(int, input().split()) -> map 객체타입 반환
  
    C에서는 long int 타입 변수 선언하여 값을 입력받아야하고
    Java에서는 long 타입 변수 선언과 long타입 입력함수를 사용해야한다.

    python에서는 기본적으로 int타입이 C언어의 long을 이용하여 구현하였다.
     0x 16진수
     0o 8진수
     전부 int타입으로 들어간다.

    
"""



