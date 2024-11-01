# 2번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
#   첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
#   첫째 줄에 A+B를 출력한다.


def solution():
    A, B = map(int, input().split())
    result = A + B
    print(result)



if __name__ == "__main__":
    solution()

"""
-Learning Point
    입력은 input() 함수로
    입력을 받을 수 있고
    한번에 입력받을때는
    map() 함수를 응용하여
    map(type, input().split()) 으로
    공백을 기준으로 여러 입력값을 받을 수 있다.
    리턴 타입은 map객체이다.

    map(function, iterable) 함수
        각각의 iterable에 function을 적용시켜 map객체로 반환하는 함수
"""