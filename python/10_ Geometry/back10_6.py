# 삼각형 외우기 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	54097	29377	26991	56.644%
# 문제
# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

# 삼각형의 세 각을 입력받은 다음,

# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.

# 입력
# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.

# 출력
# 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.


def solution(a:int, b:int, c:int) -> None:
    if a == 60 and b == 60 and c == 60:
        print("Equilateral")

    elif a + b + c == 180 and ( a == b or b == c or a == c ):
        print("Isosceles")

    elif a + b + c == 180 and a != b and b != c and a != c :
        print("Scalene")
    
    elif a + b + c != 180 :
        print("Error")

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    solution(a, b, c)


